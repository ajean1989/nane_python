from flask import Blueprint, current_app

api = Blueprint('api', __name__)

@api.route('/api')
def index():
    app = current_app  # Obtenez l'instance de l'application
    app.logger.info('Requête reçue dans le blueprint!')
    return 'Hello from your blueprint!'