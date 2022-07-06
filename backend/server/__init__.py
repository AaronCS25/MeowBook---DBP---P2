from cgitb import html
from crypt import methods
from functools import total_ordering
import json
from pickle import NONE
from tkinter import CURRENT
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
from sqlalchemy import true

from models import setup_db, Usuario, Libro, Autor, Like, Resena

# Agregar una función de paginación de ser necesario ------

LIBROS_PER_PAGE=5

def paginated_libros(request, selection):
    pagina = request.args.get('page', 1, type=int)
    inicio = (pagina - 1) * LIBROS_PER_PAGE
    final = LIBROS_PER_PAGE + inicio
    libros = [libro.format() for libro in selection]
    show_libros = libros[inicio:final]
    return show_libros


CURRENT_USER = None

# ---------------------------------------------------------

def create_app(test_config=None):
    app = Flask(__name__) # Instancia de Flask.
    setup_db(app)
    CORS(app, origins=['http://localhost:8081'], max_age=10)
    # Autorizamos a que nuestro frontend se conecte con nuestro backend.

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorizations, true')
        response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response

# Routes---------------------------------------------------

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
    #--------------------Libros--------------------#
    @app.route('/libros', methods=['GET'])
    def get_libros():
        selection = Libro.query.order_by('libro_id').all() # Todos los libros
        libros = paginated_libros(request, selection)

        if len(libros) == 0:
            abort(404)
        
        return jsonify({
            'success': True,
            'libros': libros,
            'total_libros': len(selection)
        })


# Error Handler--------------------------------------------

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

    @app.errorhandler(404)
    def forbidden(error):
        return jsonify({
            'success': False,
            'code': 404, 
            'message': 'resource not found'
        }), 404
    
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'code': 422,
            'message': 'unprocessable'
        }), 422

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            'success': False,
            'code': 500,
            'message': 'internal server error'
        }), 500
    
    return app