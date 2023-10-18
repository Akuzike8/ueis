from flask import Blueprint

card = Blueprint('card',__name__)

from controllers.card import routes
