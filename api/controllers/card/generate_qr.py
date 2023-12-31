from datetime import date
from Crypto.Hash import SHA512
from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long

import json
import os

basename = os.path.abspath('./')

def generateQr(nid):
    try:
        # importing private key
        with open(f'{basename}/keys/private.key','rb') as file:
            file = file.read()
            pvt = RSA.import_key(file)

        qid = f'{nid}-001'

        # Data to be encoded
        raw = {
            'nid':nid,
            'qr-id':qid,
            'issued_on': str(date.today())
        }

        # constructing the digital signature
        data = raw
        data = json.dumps(raw).encode()
        hash_digest = bytes_to_long(SHA512.new(data).hexdigest().encode())
        signature = hex(pow(hash_digest,pvt.d,pvt.n))
        raw['digital_signature'] = signature
        data = json.dumps(raw).encode()

        # Encoding data using make() function
        img = qrcode.make(data)

        # Generating QR code as an image file
        sig = str(signature)
        img.save(f'{basename}/cards/{qid}_qrcard.png')

        return True
    except:
        return False

with open(f'{basename}/keys/private.key','rb') as file:
            file = file.read()
            pvt = RSA.import_key(file)

# Data to be encoded
raw = "214325dsff."+str(date.today())+"."

# constructing the digital signature
data = raw.encode()
hash_digest = bytes_to_long(SHA512.new(data).hexdigest().encode())
signature = hex(pow(hash_digest,pvt.d,pvt.n))
data = raw + signature
print(len(data))
