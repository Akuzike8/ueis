from flask import Flask, request, render_template
from flask_cors import CORS
from controllers.verify_qr import verifyQr
from controllers.generate_qr import generateQr
from controllers.token import generate_token,verify_token
import json
import os

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/', methods=['GET'])
def welcome():
    return render_template('index.html')

# Scanning Page
@app.route('/scan_card', methods=['POST'])
def scan_card():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        content = request.json
        code = json.loads(content)
        status = verifyQr(code)

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

# JWT token Test route
@app.route('/token', methods=['GET'])
def generateToken():

    # Example payload data
    payload_data = "hey"

    # Generate a JWT token
    res = generate_token(payload_data)
    jwt_token = res['token']

    # Decode and verify the token
    decoded_payload = verify_token(jwt_token)

    print("Generated JWT Token:", jwt_token)
    print("Decoded Payload:", decoded_payload)
if __name__ == '__main__':
    app.run(debug=True)
