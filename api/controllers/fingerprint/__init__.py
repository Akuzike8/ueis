from flask import Blueprint

fingerprint = Blueprint('fingerprint',__name__)

from controllers.fingerprint import routes
