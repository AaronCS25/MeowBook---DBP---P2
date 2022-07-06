from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

database_name = 'meowbook'
database_path = 'postgresql://{}:{}@localhost:{}/{}'.format('postgres', '74040168', 5432,database_name) # modificar según tú contraseña

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
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(), nullable=False, unique=True)
    contrasena = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'''
                Usuario: 
                nombre = {self.nombre}
        '''
        