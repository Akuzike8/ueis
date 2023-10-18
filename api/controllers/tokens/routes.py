from controllers.tokens import token
from controllers.tokens import generate_token,verify_token
from flask import session,request

# JWT token generation route
@token.route('/token', methods=['POST'])
def generateToken():

    # Example payload data
    payload_data = request.json

    # Generate a JWT token
    res = generate_token(payload_data)
    jwt_token = res
    session['refreshToken'] = res['refresh_token']
    headers = {
        'Authorization': 'Bearer {}'.format(res['access_token']),
    }
    response = request.get('/api/Dashboard')
    return res

# JWT token verification route
@token.route('/token', methods=['GET'])
def verifyToken():
    auth_header = request.headers.get('Authorization')
    mode, token = auth_header.split(" ")

    # Decode and verify the token
    decoded_payload = token.verify_token(token)

    return decoded_payload
