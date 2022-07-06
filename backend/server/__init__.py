from cgitb import html
import json
from flask import (
    Flask, 
    jsonify,
    abort,
    render_template,
    request,
    url_for
)

from flask_cors import CORS
from itsdangerous import NoneAlgorithm

from models import setup_db, User

# Agregar una función de paginación de ser necesario ------
    


# ---------------------------------------------------------

def create_app(test_config=None):
    app = Flask(__name__) # Instancia de Flask.
    setup_db(app)
    CORS(app, origins=['http://localhost:8081'], max_age=10) # Acá se pone el url donde se levanta el frontend

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorizations, true')
        response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    @app.route('/', methods=['POST'])
    def login():
        body = request.get_json()
        nombre = body.get('nombre', None)
        contrasena = body.get('contrasena', None)

        if nombre is None or contrasena is None:
            abort(400)

        user = User.query.filter(User.nombre==nombre).filter(User.contrasena==contrasena).first()
        if user is None:
            abort(403)
        else:
            return jsonify({
                'success': True
            })

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'code': 400, 
            'message': 'bad request'
        }), 400

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            'success': False,
            'code': 403, 
            'message': 'forbidden'
        }), 403

    
    return app