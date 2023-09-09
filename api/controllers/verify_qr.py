from datetime import date
from Crypto.Hash import SHA512
from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes, bytes_to_long
import json
import os

def verifyQr(code):
    try:
        #importing public key
        basename = os.curdir
        with open(f'{basename}/keys/public.key','rb') as file:
            file = file.read()
            pub = RSA.import_key(file)

        # decoding digital signature
        raw = code
        #raw = json.loads(raw.decode())
        print(raw)
        signature = bytes_to_long(b''.fromhex(raw['digital_signature'][2:]))
        print(f'{pub.e =}')
        print(f'{pub.n =}')
        decoded_signature = long_to_bytes(pow(signature,pub.e,pub.n))

        # calculating the hash digest
        data = raw
        del data['digital_signature']
        data = json.dumps(data).encode()
        hash_digest = SHA512.new(data).hexdigest().encode()

        print(decoded_signature)
        print(hash_digest)

        if (decoded_signature == hash_digest):
            return True
        else:
            return False
    except:
        return False

