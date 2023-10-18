from controllers.identity import identity
from flask import request
from controllers.card.generate_qr import generateQr

# Registering Page
@identity.route('/create_identity', methods=['POST'])
def create_identity():
    content_type = request.headers.get('Content-Type')
    content_type = content_type.split(';')[0]

    if (content_type == 'application/json'):
        card = request.json
        status = generateQr(card['nid'])

        if (status == True):
            return {'message':'successfully created identity','status': 200}
        else:
            return {'message':'failed to create identity','status':304}

    else:
        card = request.form.to_dict()
        status = generateQr(card['nid'])

        if (status == True):
            return {'message':'successfully created identity','status': 200}
        else:
            return {'message':'failed to create identity','status':304}
