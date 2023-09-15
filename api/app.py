from flask import Flask, request, render_template,session
from flask_cors import CORS
from controllers.verify_qr import verifyQr
from controllers.generate_qr import generateQr
from controllers.token import generate_token,verify_token
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

@app.route('/', methods=['GET'])
def welcome():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

# Scanning Page
@app.route('/scan_card', methods=['POST'])
def scan_card():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        content = request.json
        code = json.loads(content)
       # status = verifyQr(code)
        status = True

        if(status == True):
            return {'message':'successfully Authenticated identity','status':200}
        else:
            return {'message':'failed to Authenticate identity', 'status': 304}

# Registering Page
@app.route('/create_identity', methods=['POST'])
def create_identity():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        card = request.form.to_dict()
        status = generateQr(card['nid'])

        if (status == True):
            return {'message':'successfully created identity','status': 200}
        else:
            return {'message':'failed to create identity','status':304}

# JWT token generation route
@app.route('/token', methods=['POST'])
def generateToken():

    # Example payload data
    payload_data = request.json

    # Generate a JWT token
    res = generate_token(payload_data)
    jwt_token = res
    session['refreshToken'] = res['refresh_token']
    return res

# JWT token verification route
@app.route('/token', methods=['GET'])
def verifyToken():
    auth_header = request.headers.get('Authorization')
    mode, token = auth_header.split(" ")

    # Decode and verify the token
    decoded_payload = verify_token(token)

    return decoded_payload

if __name__ == '__main__':
    app.run(debug=True)
