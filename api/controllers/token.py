import os
import jwt
import datetime
from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes


def generate_token(payload):
    #try:
        #load secret key
        basename = os.curdir
        with open(f'{basename}/keys/private.key','rb') as file:
            file = file.read()
            pvt = RSA.import_key(file)
            SECRET_KEY = long_to_bytes(pvt.d)

        # Set the expiration time, it's set to expire in 1 hour
        expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=1)

        # Create the JWT token
        token = jwt.encode(
            {
                'exp': expiration,
                'payload': payload,
            },
            SECRET_KEY,
            algorithm='HS256'  # You can choose the signing algorithm you prefer
        )

        return {'message':'JWT generated','token':token,'status':200}
    #except:
     #   return {'message':'Failed to generate token','status':401}

def verify_token(token):
    try:
        #load secret key
        basename = os.curdir
        with open(f'{basename}/keys/private.key','rb') as file:
            file = file.read()
            pvt = RSA.import_key(file)
            SECRET_KEY = long_to_bytes(pvt.d)

        # Decode and verify the token
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload

    except jwt.ExpiredSignatureError:
        # Token has expired
        return {'error': 'Token has expired','status':401}
    except jwt.InvalidTokenError:
        # Token is invalid
        return {'error': 'Invalid token','status':401}

def generate_csrf_token():
    return {'message':'csrf token generated'}

def verify_csrf_token():
    return {'message':'csrf token verified'}
