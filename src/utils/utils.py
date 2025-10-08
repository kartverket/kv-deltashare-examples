import os
import subprocess
import json
import requests
from datetime import datetime, timezone
from google.auth import identity_pool
from google.cloud import storage

DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"

def create_credentials_config(provider, TOKEN_FILE, CREDENTIALS_FILE):
    
    subprocess.run([
        "gcloud", "iam", "workload-identity-pools", "create-cred-config",
        provider, "--credential-source-type=text",
        f"--credential-source-file={TOKEN_FILE}",
        f"--output-file={CREDENTIALS_FILE}"
    ], check=True)


def fetch_config_share(bucket_id, SHARE_FILE_PATH, CREDENTIALS_FILE):
    if is_config_expired(SHARE_FILE_PATH):
        print("config is expired or missing, downloading a new one...")
        filename = "config.share"

        #subprocess.run(["gcloud", "auth", "login", "--cred-file", CREDENTIALS_FILE, "--quiet"], check=True)
        #gcs_path = f"gs://{bucket_id}/{filename}"
        #subprocess.run(["gcloud", "storage", "cp", gcs_path, SHARE_FILE_PATH], check=True)

 
        credentials = identity_pool.Credentials.from_file(CREDENTIALS_FILE)
        storage_client = storage.Client(credentials = credentials)
        bucket = storage_client.bucket(bucket_id)

        blob = bucket.blob(filename)
        blob.download_to_filename(SHARE_FILE_PATH)
        print("Downloaded storage object {} from bucket {} to local file {}.".format( bucket_id, filename, SHARE_FILE_PATH))
    else:
        print("config.share er gyldig")
        
def read_json(file_path):
    if not os.path.exists(file_path):
        return None
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Error reading {file_path}: {e}")
        return None
    
def create_credentials_config(provider, TOKEN_FILE, CREDENTIALS_FILE):
    
    subprocess.run([
        "gcloud", "iam", "workload-identity-pools", "create-cred-config",
        provider, "--credential-source-type=text",
        f"--credential-source-file={TOKEN_FILE}",
        f"--output-file={CREDENTIALS_FILE}"
    ], check=True)



def fetch_config_share(project_id, bucket_id, SHARE_FILE_PATH, CREDENTIALS_FILE):
    if is_config_expired(SHARE_FILE_PATH):
        print("config is expired or missing, downloading a new one...")
        filename = "config.share"
 
        credentials = identity_pool.Credentials.from_file(CREDENTIALS_FILE)
        storage_client = storage.Client(project_id, credentials = credentials)
        bucket = storage_client.bucket(bucket_id)

        blob = bucket.blob(filename)
        blob.download_to_filename(SHARE_FILE_PATH)
        print("Downloaded storage object {} from bucket {} to local file {}.".format( bucket_id, filename, SHARE_FILE_PATH))
    else:
        print("config.share er gyldig")

def write_json(file_path, data):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

def is_auth_valid(auth_path):
    if not os.path.exists(auth_path):
        return False
    try:
        with open(auth_path, "r") as f:
            auth_data = json.load(f)
        expiration_time = datetime.fromisoformat(auth_data["expiration_time"]).replace(tzinfo=timezone.utc)
        if expiration_time < datetime.now(timezone.utc):
            print(f"Authentication expired at {expiration_time}. Fetching a new one...")
            return False
        print(f"Valid authentication found. Expires at {expiration_time}.")
        return True
    except (json.JSONDecodeError, ValueError, KeyError):
        print("Invalid authentication file.")
        return False

def is_config_expired(config_path):
    config = read_json(config_path)
    if not config:
        return True
    required_keys = ["shareCredentialsVersion", "bearerToken", "endpoint", "expirationTime"]
    if not all(key in config for key in required_keys):
        print("Invalid share config: Missing required keys.")
        return True
    try:
        expiration_time = datetime.strptime(config["expirationTime"], DATETIME_FORMAT).replace(tzinfo=timezone.utc)
        if expiration_time < datetime.now(timezone.utc):
            print(f"Share credentials expired at {expiration_time}. Need to fetch a new one...")
            return True
        print("Valid Delta Sharing configuration found.")
        return False
    except ValueError:
        print("Error: Invalid expirationTime format in config file.")
        return True
