import uuid
from jwcrypto import jwk, jwt
from datetime import datetime, timezone
import requests


def generate_maskinporten_token(
    client_id,
    scope,
    audience,
    kid,
    certname,
    token_url,
    cert_password=None
):
    timestamp = int(datetime.now(timezone.utc).timestamp())

    with open(certname, mode='rb') as f:
        key = jwk.JWK.from_pem(
            data=f.read(),
            password=cert_password.encode() if cert_password else None
        )

    jwt_header = {
        'alg': 'RS256',
        'kid': kid
    }

    jwt_claims = {
        'iss': client_id,         
        'sub': client_id,         
        'aud': token_url,
        'iat': timestamp,
        'exp': timestamp + 120,
        'jti': str(uuid.uuid4()),
        'scope': scope,
        'resource': audience      
    }

    jwt_token = jwt.JWT(header=jwt_header, claims=jwt_claims)
    jwt_token.make_signed_token(key)
    signed_jwt = jwt_token.serialize()
    
   

    return signed_jwt

def generate_access_token(
    client_id,
    scope,
    audience,
    kid,
    certname,
    token_url,
    cert_password=None
): 
    client_assertion = generate_maskinporten_token(
        client_id=client_id,
        scope=scope,
        audience=audience,
        kid=kid,
        certname=certname,
        token_url=token_url,
        cert_password=cert_password
    )
    
    body = {
        "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
        "assertion": client_assertion
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = requests.post(token_url, data=body, headers=headers)
    return response.json()

