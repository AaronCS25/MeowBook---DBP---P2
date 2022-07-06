from importlib.metadata import SelectableGroups
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, delete, true

#-------------------------

database_name = 'meowbook'
password_path = '1234'
database_path = 'postgresql://{}:{}@localhost:{}/{}'.format('postgres', password_path, 5432,database_name)

#--------------------------


db = SQLAlchemy() # Instancia SQL

def setup_db(app, database_path=database_path):
    # Configuraciones de la instancia -------------------
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app) # Inicialización de la app----------
    db.create_all()  # Creación de modelos.--------------

# Modelos -----------------------------------------------------------
#------------------------------Usuario------------------------------#
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    usuario_id = db.Column(db.Integer, primary_key=True)
    usuario_nombre = db.Column(db.String, nullable=False)
    usuario_apellido = db.Column(db.String, nullable=False)
    usuario_nacimiento = db.Column(db.Date, nullable=False)
    usuario_email = db.Column(db.String, unique=True, nullable=False)
    usuario_apodo = db.Column(db.String, unique=True, nullable=False)
    usuario_contrasena = db.Column(db.String, nullable=False)
    likes = db.relationship('Like', backref='Usuario')
    resenas = db.relationship('Resena', backref='Usuario')

    def __repr__(self):
        return f'''
                Usuario: 
                id = {self.usuario_id}, 
                nombre = {self.usuario_nombre}, 
                apellido = {self.usuario_apellido}, 
                fecha_nacimiento = {self.usuario_nacimiento}, 
                email = {self.usuario_email}, 
                user = {self.usuario_apodo}, 
                password = {self.usuario_contrasena}
        '''

#-------------------------------Libro-------------------------------#
class Libro(db.Model):
    __tablename__ = 'libros'
    libro_id = db.Column(db.Integer, primary_key=True)
    libro_titulo = db.Column(db.Integer, nullable=False)
    libro_autor_id = db.Column(db.Integer, ForeignKey('autores.autor_id'))
    libro_sinopsis = db.Column(db.Text, nullable=False)
    libro_editorial = db.Column(db.String, nullable=False)
    libro_publicacion = db.Column(db.Date, nullable=True)
    libro_isbn = db.Column(db.String, nullable=False)
    resenas = db.relationship('Resena', backref='Libro')

    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.libro_id
        except:
            db.session.rollback()
        finally:
            db.session.close()
    
    def update(self):
        try:
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
    
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
        
    def format(self):
        return {
            'id': self.libro_id,
            'libro_titulo': self.libro_titulo,
            'libro_autor_id': self.libro_autor_id,
            'libro_isbn': self.libro_isbn
        }

    def __repr__(self):
        return f'''
                Libro: 
                id = {self.libro_id}, 
                autor_id = {self.libro_autor_id},  
                titulo = {self.libro_titulo}, 
                editorial = {self.libro_editorial}, 
                publicacion = {self.libro_publicacion}, 
                ISBN = {self.libro_isbn}
        '''

#-------------------------------Autor-------------------------------#
class Autor(db.Model):
    __tablename__ = 'autores'
    autor_id = db.Column(db.Integer, primary_key=True)
    autor_nombre = db.Column(db.String, nullable=False)
    autor_apellido = db.Column(db.String, nullable=True)
    autor_estado = db.Column(db.Boolean, nullable=False)
    libros = db.relationship('Libro', backref='Autor')

    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.autor_id
        except:
            db.session.rollback()
        finally:
            db.session.close()
    
    def update(self):
        try:
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
    
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
        
    def format(self):
        return {
            'id': self.autor_id,
            'autor_nombre': self.autor_nombre,
            'autor_apellido': self.autor_apellido,
            'autor_estado': self.autor_estado
        }

    def __repr__(self):
        return f'''
                Autor: 
                id = {self.autor_id}, 
                nombre = {self.autor_nombre}, 
                apellido = {self.autor_apellido}, 
                estado = {self.autor_estado}
        '''

#--------------------------------Like-------------------------------#
class Like(db.Model):
    __tablename__ = 'likes'
    like_id = db.Column(db.Integer, primary_key=True)
    like_usuario_id = db.Column(db.Integer, ForeignKey('usuarios.usuario_id'))
    like_libro_id = db.Column(db.Integer, ForeignKey('libros.libro_id'))

    def __repr__(self):
        return f'''
                Like:
                id = {self.like_id}, 
                usuario_id = {self.like_usuario_id}, 
                libro_id = {self.like_libro_id}
        '''

#-------------------------------Resena------------------------------#
class Resena(db.Model):
    __tablename__ = 'resenas'
    resena_id = db.Column(db.Integer, primary_key=True)
    resena_usuario_id = db.Column(db.Integer, ForeignKey('usuarios.usuario_id'))
    resena_libro_id = db.Column(db.Integer, ForeignKey('libros.libro_id'))
    resena_comentario = db.Column(db.Text, nullable=False)
    # resena_like -> Por investigar
    resena_publicacion = db.Column(db.Date, nullable=False) # Default = currend_date

    def __repr__(self):
        return f'''
                Resena:
                id = {self.resena_id}, 
                usuario_id = {self.resena_usuario_id}, 
                libro_id = {self.resena_libro_id}
                publicacion = {self.resena_publicacion}
        '''