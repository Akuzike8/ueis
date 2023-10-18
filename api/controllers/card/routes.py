from controllers.card import card
from controllers.card.verify_qr import verifyQr
from requests import request

# Scanning Page
@card.route('/scan_card', methods=['POST'])
def scan_card():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        card = request.json
        status = verifyQr(card)

        if(status == True):
            return {'message':'successfully Authenticated identity','status':200}
        else:
            return {'message':'failed to Authenticate identity', 'status': 304}
