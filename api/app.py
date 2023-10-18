from flask import Flask, request, render_template,session
from flask_cors import CORS
from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes
import json
import os

basename = os.curdir
with open(f'{basename}/keys/private.key','rb') as file:
    file = file.read()
    pvt = RSA.import_key(file)
    SECRET_KEY = long_to_bytes(pvt.d)

app = Flask(__name__)
app.secret_key = SECRET_KEY
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# Register Route blueprints
from controllers.card import card
app.register_blueprint(card)

from controllers.fingerprint import fingerprint
app.register_blueprint(fingerprint)

from controllers.identity import identity
app.register_blueprint(identity)

from controllers.tokens import token
app.register_blueprint(token)

@app.route('/', methods=['GET'])
def welcome():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/fingerprint', methods=['GET'])
def fingerprint():
    return render_template('fingerprint_auth.html')

if __name__ == '__main__':
    app.run(debug=True)
