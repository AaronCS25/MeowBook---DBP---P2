import unittest
from flask_sqlalchemy import SQLAlchemy

from server import create_app
from models import setup_db, Autor, Libro
import json

class TestCaseTodoApp(unittest.TestCase):

    def setUp(self):
        self.app = create_app() # Instancia de la aplicación.
        self.client = self.app.test_client
        self.database_name = 'meowbook_test'
        self.database_path = 'postgresql://{}:{}@localhost:{}/{}'.format('postgres', 'Magdalena150', 5432,self.database_name)

        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

        self.newAutor = {
            'autor_nombre':'autor_nombre_test',
            'autor_apellido': 'autor_apellido_test',
            'autor_estado': True
        }

        self.newAutor_search = {
            'search': 'Mario'
        }

        self.newLibro = {
            'libro_titulo': 'libro test',
            'libro_autor_id': 1,
            'libro_sinopsis': 'sinopsis test',
            'libro_editorial': 'editorial test',
            'libro_publicacion': 'publicacion test',
            'libro_isbn': 'isbn test'
        }


#--------------------Autor_Test---------------------#
    @unittest.skip('TEST PASS')
    def test_get_autor_successfully(self):
        res = self.client().get('/autores')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['autores'])
        self.assertTrue(data['total_autoress'])

    @unittest.skip('TEST PASS')
    def test_get_autor_unsuccessfully(self):
        res = self.client().get('/autoress')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])

    @unittest.skip('TEST PASS')
    def test_create_autor_successfully(self):
        res = self.client().post('/autores', json = self.newAutor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['autores'])
        self.assertTrue(data['total_autores'])

    @unittest.skip('TEST PASS')
    def test_create_autor_unsuccessfully(self):
        res = self.client().post('/autores', json = {})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')
        self.assertTrue(data['message'])

    @unittest.skip('TEST PASS')
    def test_get_autor_by_nombre_successfully(self):
        res = self.client().post('/autores', json = self.newAutor_search)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['autores'][0]['autor_nombre'], 'Mario' )
        pass

    @unittest.skip('TEST PASS')
    def test_get_autor_by_nombre_empty(self):
        res = self.client().post('/autores', json = {'search': '0'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['autores'], [] )
        pass

    @unittest.skip('TEST PASS')    
    def test_update_autores_by_id_successfully(self):
        res = self.client().patch('/autores/1', json = {'autor_nombre': 'update_nombre'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['autor_id'], '1')
        pass

    @unittest.skip('TEST PASS') 
    def test_update_autores_by_id_unsuccessfully(self):
        res = self.client().patch('/autores/-1', json = {'autor_nombre': 'update_nombre'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])

    @unittest.skip('TEST PASS') 
    def test_delete_autores_by_id_successfully(self):
        res = self.client().delete('/autores/10')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        pass

    @unittest.skip('TEST PASS') 
    def test_delete_autores_by_id_unsuccessfully(self):
        res = self.client().delete('/autores/-10')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])
        pass

#--------------------Libros_Test--------------------#
    @unittest.skip('TEST PASS') 
    def test_get_libros_successfully(self):
        res = self.client().get('/libros')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        pass

    @unittest.skip('TEST PASS') 
    def test_get_libros_unsuccessfully(self):
        res = self.client().get('/libross')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        pass
        

    @unittest.skip('TEST PASS') 
    def test_create_libros_successfully(self):
        res = self.client().post('/libros', json=self.newLibro)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        pass
        

    @unittest.skip('TEST PASS') 
    def test_create_libros_unsuccessfully(self):
        res = self.client().post('/libros', json={})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        pass

    @unittest.skip('TEST PASS') 
    def test_search_libros_by_id_successfully(self):
        res = self.client().post('/libros/1', json = self.newAutor_search)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['autores'][0]['autor_nombre'], 'Mario' )
        pass

    @unittest.skip('TEST PASS') 
    def test_search_libros_by_id_unsuccessfully(self):
        res = self.client().post('/libros/1', json = self.newAutor_search)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['autores'][0]['autor_nombre'], 'Mario' )
        pass

    @unittest.skip('TEST PASS') 
    def test_update_libros_by_id_successfully(self):
        res = self.client().patch('/libros/1', json = {'autor_nombre': 'update_nombre'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['autor_id'], '1')
        pass

    @unittest.skip('TEST PASS') 
    def test_update_libros_by_id_unsuccessfully(self):
        res = self.client().patch('/libros/-1', json = {})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        pass
        

    @unittest.skip('TEST PASS') 
    def test_delete_libros_by_id_successfully(self):
        res = self.client().delete('/libros/3')
        data = json.loads(res.data)
        print('data: ', data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        pass
        

    @unittest.skip('TEST PASS') 
    def test_delete_libros_by_id_unsuccessfully(self):
        res = self.client().delete('/libros/-3')
        data = json.loads(res.data)
        print('data: ', data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        pass

    @unittest.skip('TEST PASS') 
    def test_get_like_successfully(self):
        res = self.client().get('/likes')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        pass
        

    @unittest.skip('TEST PASS')
    def test_get_like_unsuccessfully(self):
        res = self.client().get('/likess')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        pass

    @unittest.skip('TEST PASS')
    def test_search_like_successfully(self):
        res = self.client().get('/likes')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        pass

    @unittest.skip('TEST PASS')
    def test_search_like_unsuccessfully(self):
        res = self.client().get('/likess')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        pass

    @unittest.skip('TEST PASS')
    def test_create_like_successfully(self):
        res = self.client().post('/libros', json=self.newLibro)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        pass

    @unittest.skip('TEST PASS')
    def test_create_like_unsuccessfully(self):
        res = self.client().post('/libros', json=self.newLibro)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        pass
    
    @unittest.skip('TEST PASS')
    def test_delete_like_successfully(self):
        res = self.client().delete('/likes/2')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        pass

    @unittest.skip('TEST PASS')
    def test_delete_like_unsuccessfully(self):
        res = self.client().delete('/likes/-2')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        pass

    def tearDown(self):
        pass