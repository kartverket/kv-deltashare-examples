import ast
import json
import base64
import pandas as pd
import re
from Crypto.Cipher import ChaCha20_Poly1305, PKCS1_OAEP
from Crypto.PublicKey import RSA

# --- Config ---


delta_share_ref = ""
encrypted_table_name = "dim_kulturminner_encrypted.csv"
keys_encrypted_table_name = f"keys_encrypted_{delta_share_ref}.csv"
private_key_path = "crypto/consumer_private_key.pem"
skip_cols = {
    "kulturminneId", "keyId", "versjon", "versjonId",
    "from_datetime", "to_datetime", "symmetric_key"
}

# --- Decryption Helpers ---


def decode_base64_with_padding(b64_str):
    if pd.isna(b64_str):
        return b""
    b64_str = b64_str.strip()
    missing_padding = len(b64_str) % 4
    if missing_padding:
        b64_str += "=" * (4 - missing_padding)
    return base64.b64decode(b64_str)


def parse_encrypted_json(b64_encoded_json):
    try:
        decoded = decode_base64_with_padding(b64_encoded_json)
        parsed = json.loads(decoded)
        return decode_base64_with_padding(parsed["ciphertext"]), decode_base64_with_padding(parsed["nonce"])
    except Exception:
        return None, None


def parse_encrypted_key(cell):
    if isinstance(cell, bytes):
        return cell
    if isinstance(cell, str):
        s = cell.strip()
        # Old format: Python literal like b'...'
        if s.startswith("b'") or s.startswith('b"') or s.startswith('['):
            return ast.literal_eval(s)
        # New format: Base64 string
        return decode_base64_with_padding(s)
    raise TypeError(f"Unsupported type for encrypted key: {type(cell)}")


def asymmetric_decrypt_symmetric_key(encrypted_key, private_key_bytes):
    rsa_key = RSA.importKey(private_key_bytes)
    cipher = PKCS1_OAEP.new(rsa_key)
    return cipher.decrypt(encrypted_key)


def symmetric_decrypt_data(ciphertext, key, nonce):
    cipher = ChaCha20_Poly1305.new(key=key, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext[:-16], ciphertext[-16:])


def try_decrypt_field(value, key):
    if not isinstance(value, str):
        return None
    ciphertext, nonce = parse_encrypted_json(value)
    if ciphertext and nonce:
        try:
            return symmetric_decrypt_data(ciphertext, key, nonce).decode("utf-8")
        except Exception as e:
            print(
                f"Decryption failed: {e} - Value starts with: {value[:50]}...")
    return None

# --- String Cleaners ---


def clean_numpy_array_string(text):
    if isinstance(text, str):
        pattern = r"array\((\[[^\]]*\])(?:,\s*dtype=[^\)]*)?\)"
        text = re.sub(pattern, r"\1", text, flags=re.DOTALL)
    return text


def fix_missing_commas(text):
    if isinstance(text, str):
        text = re.sub(r'\}\s*\{', '}, {', text)
        text = re.sub(r'\]\s*\{', '], {', text)
        text = re.sub(r'\}\s*\[', '}, [', text)
    return text

# --- Recursive Decryption ---


def recursive_decrypt(value, key):
    if isinstance(value, str):
        value = clean_numpy_array_string(value).strip()
        if (value.startswith("{") and value.endswith("}")) or (value.startswith("[") and value.endswith("]")):
            value = fix_missing_commas(value)
            try:
                parsed = ast.literal_eval(value)
                return recursive_decrypt(parsed, key)
            except Exception as e:
                print(f"Failed parsing, trying direct decrypt: {e}")
        decrypted = try_decrypt_field(value, key)
        return decrypted if decrypted is not None else value
    elif isinstance(value, dict):
        return {k: recursive_decrypt(v, key) for k, v in value.items()}
    elif isinstance(value, list):
        return [recursive_decrypt(v, key) for v in value]
    else:
        return value

# --- Main Logic ---


def load_and_decrypt(delta_share_ref=None, strict_mode=True):
    # Load private key
    with open(private_key_path, "rb") as f:
        private_key = f.read()

    keys_encrypted_table_name = f"keys_encrypted_{delta_share_ref}.csv"

    # Decrypt symmetric keys
    df_data = pd.read_csv(encrypted_table_name)

    # Get all unique key IDs from the data
    used_key_ids = df_data["keyId"].dropna().unique()

    # Load key file and filter only used keyIds
    df_keys = pd.read_csv(keys_encrypted_table_name)

    df_keys = df_keys[df_keys["key_id"].isin(used_key_ids)]

    key_map = {}
    for _, row in df_keys.iterrows():
        try:
            encrypted_key_bytes = parse_encrypted_key(row["encrypted_keys"])
            symmetric_key = asymmetric_decrypt_symmetric_key(
                encrypted_key_bytes, private_key)
            key_map[row["key_id"]] = symmetric_key
        except Exception as e:
            error_msg = f"Failed to decrypt key_id {row['key_id']}: {e}"
            if strict_mode:
                raise RuntimeError(error_msg)
            print(error_msg)
            key_map[row["key_id"]] = None

    # Load encrypted data
    df_data["symmetric_key"] = df_data["keyId"].map(key_map)

    # Decrypt fields
    for col in df_data.columns:
        if col in skip_cols:
            continue
        df_data[col] = df_data.apply(
            lambda row: recursive_decrypt(row[col], row["symmetric_key"]) if isinstance(
                row["symmetric_key"], bytes) else None,
            axis=1
        )

    # Cleanup
    df_data = df_data.drop(columns=["symmetric_key"])
    df_data.to_csv(f"decrypted_{delta_share_ref}_data.csv", index=False)
    print(
        f"\nDecryption complete. Saved to decrypted_{delta_share_ref}_data.csv")


if __name__ == "__main__":
    load_and_decrypt(delta_share_ref)
