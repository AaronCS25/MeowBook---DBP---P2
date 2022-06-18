from crypt import methods
import json
import re
from flask import (
    Flask, 
    jsonify,
    abort,
    render_template,
    request
)

from flask_cors import CORS
from itsdangerous import NoneAlgorithm

from models import setup_db, Usuario, Libro, Autor, Resena


# Agregar una función de paginación de ser necesario ------
    # TODO


# ---------------------------------------------------------

def create_app(test_config=None):
    app = Flask(__name__) # Instancia de Flask.
    setup_db(app)
    # CORS(app) -> Que se necesita?

    # @app.after_request
    # def after_request(response):
    #     response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorizations, true')
    #     response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PATCH,DELETE,OPTIONS')
    #     return response

    @app.route('/')
    def index():
        return render_template('index.hmtl')