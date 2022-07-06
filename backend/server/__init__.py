from distutils.log import error
import json
from tkinter.messagebox import NO
from tkinter.tix import Tree
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
AUTORES_PER_PAGE=5
LIKES_PER_PAGE=5

def paginated_autores(request, selection):
    pagina = request.args.get('page', 1, type=int)
    inicio = (pagina - 1) * LIBROS_PER_PAGE
    final = LIBROS_PER_PAGE + inicio
    autores = [autor.format() for autor in selection]
    show_autores = autores[inicio:final]
    return show_autores

def paginated_libros(request, selection):
    pagina = request.args.get('page', 1, type=int)
    inicio = (pagina - 1) * LIBROS_PER_PAGE
    final = LIBROS_PER_PAGE + inicio
    libros = [libro.format() for libro in selection]
    show_libros = libros[inicio:final]
    return show_libros

def paginated_likes(request, selection):
    pagina = request.args.get('page', 1, type=int)
    inicio = (pagina - 1) * LIKES_PER_PAGE
    final = LIKES_PER_PAGE + inicio
    likes = [like.format() for like in selection]
    show_likes = likes[inicio:final]
    return show_likes


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

    #--------------------Autor---------------------#
    @app.route('/autores', methods=['GET'])
    def get_autor():
        selection = Autor.query.order_by('autor_id').all()
        autores = paginated_autores(request, selection)

        if len(autores) == 0:
            abort(404)
        
        return jsonify({
            'success': True,
            'autores': autores,
            'total_autoress': len(autores)
        })

    @app.route('/autores', methods=['POST'])
    def create_autores():
        body = request.get_json()
        error_422=False

        autor_nombre = body.get('autor_nombre', None)
        autor_apellido = body.get('autor_apellido', None)
        autor_estado = body.get('autor_estado', 'activo')
        search = body.get('search', None)

        if search:
            selection = Autor.query.order_by('autor_id').filter(Autor.autor_nombre.like('%{}%'.format(search))).all()
            autores = paginated_autores(request, selection)
            return jsonify({
                'success': True,
                'autores': autores,
                'total_autores': len(selection)
            })

        try:
            if autor_nombre is None or autor_apellido is None or autor_estado is None:
                error_422=True
                abort(422)
                
            
            autor = Autor(  autor_nombre=autor_nombre,
                            autor_apellido=autor_apellido,
                            autor_estado=autor_estado)
            
            new_autor_id = autor.insert()

            selection = Autor.query.order_by('autor_id').all()
            autores = paginated_autores(request, selection)

            return jsonify({
                'success': True,
                'created': new_autor_id,
                'autores': autores,
                'total_autores': len(selection)
            })
        except Exception as e:
            print(e)
            if error_422:
                abort(422)
            else:
                abort(500)
    
    @app.route('/autores/<autor_id>', methods=['PATCH'])
    def updated_autor(autor_id):
        error_404=False
        try:
            autor = Autor.query.filter(Autor.autor_id == autor_id).one_or_none()
            if autor is None:
                error_404=True
                abort(404)

            body = request.get_json()
            if 'autor_nombre' in body:
                autor.autor_nombre = body.get('autor_nombre')
            if 'autor_apellido' in body:
                autor.autor_apellido = body.get('autor_apellido')
            if 'autor_estado' in body:
                autor.autor_estado = body.get('autor_estado')

            autor.update()

            return jsonify({
                'success': True,
                'autor_id': autor_id
            })

        except Exception as e:
            print(e)
            if error_404:
                abort(404)
            else:
                abort(500)
    
    @app.route('/autores/<autor_id>', methods=['DELETE'])
    def delete_autor(autor_id):
        error_404 = False
        try:
            autor = Autor.query.filter(Autor.autor_id == autor_id).one_or_none()
            if autor is None:
                error_404=True
                abort(404)
            
            autor.delete()

            selection = Autor.query.oder_by('id').all()
            autores = paginated_autores(request, selection)

            return jsonify({
                'success': True,
                'deleted': autor_id,
                'autores': autores,
                'total_autores': len(selection)
            })
        except Exception as e:
            print(e)
            if error_404:
                abort(404)
            else:
                abort(500)

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
    
    @app.route('/libros', methods=['POST'])
    def create_libro():
        body = request.get_json()

        libro_titulo = body.get('libro_titulo', None)
        libro_autor_id = body.get('libro_autor_id', 1)
        libro_sinopsis = body.get('libro_sinopsis', None)
        libro_editorial = body.get('libro_editorial', None)
        libro_publicacion = body.get('libro_publicacion', None)
        libro_isbn = body.get('libro_isbn', None)

        search = body.get('search', None)

        if search:
            selection = Libro.query.oder_by('libro_id').filter(Libro.libro_titulo.like('%{}%'.format(search))).all()
            libros = paginated_libros(selection)
            return jsonify({
                'success': True,
                'libros': libros,
                'total_libros': len(selection)
            })
        
        if libro_titulo is None or libro_autor_id is None or libro_sinopsis is None or libro_editorial is None or libro_publicacion is None or libro_isbn is None:
            abort(422)
        
        try:
            libro = Libro(  libro_titulo=libro_titulo,
                            libro_autor_id=libro_autor_id,
                            libro_sinopsis=libro_sinopsis,
                            libro_editorial=libro_editorial, 
                            libro_publicacion=libro_publicacion, 
                            libro_isbn=libro_isbn)

            new_libro_id = libro.insert()

            selection = Libro.query.oder_by('libro_id').all()
            libros = paginated_libros(request, selection)

            return jsonify({
                'success': True,
                'created': new_libro_id,
                'libros': libros,
                'total_libros': len(selection)
            })
        except Exception as e:
            print(e)
            abort(500)

    @app.route('/libros/<libro_id>', methods=['PATCH'])
    def update_libro(libro_id):
        error_404 = False
        try:
            libro = Libro.query.filter(Libro.libro_id == libro_id).one_or_none()
            if libro is None:
                error_404 = True
                abort(404)

            body = request.get_json()
            if 'libro_titulo' in body:
                libro.libro_titulo = body.get('libro_titulo')
            if 'libro_autor_id' in body:
                libro.libro_titulo = body.get('libro_titulo')
            if 'libro_sinopsis' in body:
                libro.libro_sinopsis = body.get('libro_sinopsi')
            if 'libro_editorial' in body:
                libro.libro_editorial = body.get('libro_editorial')
            if 'libro_publicacion' in body:
                libro.libro_publicacion = body.get('libro_publicacion')
            if 'libro_isbn' in body:
                libro.libro_isbn = body.get('libro_isbn')

            libro.update()

            return jsonify({
                'success': True,
                'libro_id': libro_id
            })
        except Exception as e:
            print(e)
            if error_404:
                abort(404)
            else:
                abort(500)

    @app.route('/libros/<libro_id>', methods=['DELETE'])
    def delete_libro(libro_id):
        error_404 = False
        try:
            libro = Libro.query.filter(Libro.id == libro_id).one_or_none()
            if libro is None:
                error_404 = True
                abort(404)
            
            libro.delete()

            selection = Libro.query.order_by('libro_id').all()
            libros = paginated_libros(request, selection)

            return jsonify({
                'success': True,
                'deleted': libro_id,
                'libros': libros,
                'total_libros': len(selection)
            })
        except Exception as e:
            print(e)
            if error_404:
                abort(404)
            else:
                abort(500)

    #---------------------Like---------------------#
    @app.route('/likes', methods=['GET']) # Retorna los libros que nos gustan.
    def get_likes():
        selection = Like.query.order_by('like_id').all()
        likes = paginated_likes(request, selection)

        if len(likes) == 0:
            abort(404)
        
        return jsonify({
            'succes': True,
            'likes': likes,
            'total_likes': len(selection)
        })
    
    @app.route('/likes', methods=['POST'])
    def create_like():
        body = request.get_json()
        like_usuario_id = body.get('like_usuario_id', None)
        like_libro_id = body.get('like_libro_id', None)
        search = body.get('search', None)

        if search:
            # Fix selection.
            selection = Libro.query.order_by('libro_id').filter(Libro.libro_titulo.like('%{}%'.format(search))).all()
            # Fix likes
            likes = paginated_likes(request, selection)
            return jsonify({
                'success': True,
                'like_libros': likes,
                'total_likes': len(selection)
            })
        if like_usuario_id is None or like_libro_id is None:
            abort(422)
        
        try:
            like = Like( like_usuario_id=like_usuario_id,
                         like_libro_id=like_libro_id)
            new_like_id = like.insert()

            selection = Like.query.order_by('like_id').all()
            likes = paginated_likes(request, selection)

            return jsonify({
                'success': True,
                'created': new_like_id,
                'likes': likes,
                'total_likes': len(selection)
            })
        except Exception as e:
            print(e)
            abort(500)

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