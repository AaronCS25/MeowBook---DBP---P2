from asyncio import FastChildWatcher
from enum import unique
from flask_sqlalchemy import SQLAlchemy

database_name = 'meowbook'
database_path = 'postgresql://{}:{}@localhost:{}/{}'.format('postgres', '1234', 5432,database_name)

db = SQLAlchemy() # Instancia SQL

def setup_db(app, database_path=database_path):
    # Configuraciones de la instancia -------------------
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app) # Inicialización de la app----------
    db.create_all()  # Creación de modelos.--------------

# Modelos -----------------------------------------------

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    usuario_id = db.Column(db.Integer, primary_key=True)
    usuario_nombre = db.Column(db.String, nullable=False)
    usuario_apellido = db.Column(db.String, nullable=False)
    usuario_nacimiento = db.Column(db.Date, nullable=False)
    usuario_email = db.Column(db.String, unique=True, nullable=False)
    usuario_apodo = db.Column(db.String, unique=True, nullable=False)
    usuario_contrasena = db.Column(db.String, nullable=False)

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


