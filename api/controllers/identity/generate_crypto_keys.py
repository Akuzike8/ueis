from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes, bytes_to_long
import os

keys = RSA.generate(2048)
pub = keys.public_key()
pub = pub.export_key()
keys = keys.export_key()

basename = os.path.abspath

with open(f'{basename}/keys/new-private.key','wb') as file:
    file.write(keys)

with open(f'{basename}/keys/new-public.key','wb') as file:
    file.write(pub)
