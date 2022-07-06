from cgitb import html
import json
from urllib import response
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

from models import setup_db, Usuario

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

    @app.route('/usuarios', methods=['POST'])
    def create_usuario():
        usuario_nombre = request.get_json()['usuario_nombre']
        usuario_apellido = request.get_json()['usuario_apellido']
        usuario_nacimiento = request.get_json()['usuario_nacimiento']
        usuario_email = request.get_json()['usuario_email']
        usuario_apodo = request.get_json()['usuario_apodo']
        usuario_contrasena = request.get_json()['usuario_contrasena']

        usuario = Usuario(usuario_nombre=usuario_nombre, usuario_apellido=usuario_apellido, usuario_nacimiento=usuario_nacimiento, usuario_email=usuario_email, usuario_apodo=usuario_apodo, usuario_contrasena=usuario_contrasena)
        new_usuario = usuario.insert()

        return jsonify({
            'success': True,
            'created': new_usuario
        })
        


    @app.route('/', methods=['POST'])
    def login():
        body = request.get_json()
        usuario_email = body.get('usuario_email', None)
        usuario_contrasena = body.get('usuario_contrasena', None)

        if usuario_email is None or usuario_contrasena is None:
            abort(400)

        usuario = Usuario.query.filter(Usuario.usuario_email==usuario_email).filter(Usuario.usuario_contrasena==usuario_contrasena).first()
        if usuario is None:
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