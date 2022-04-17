from flask_testing import TestCase
from flask import current_app, url_for
from main import app
from app.models import db

class MainTest(TestCase):
    # regresar una aplicacion app de flask
    def create_app(self):
        app.config['TESTING']= True
        app.config['WTF_CSRF_ENABLED']= False   #no tenemos session activa de usuario

        return app

    def test_app_exists(self):
        # prueba que la app existe
        self.assertIsNotNone(current_app)

    def test_app_test_mode(self):
        # prueba que la app esta en modo testing
        self.assertTrue(current_app.config['TESTING'])

    def test_index_redirects(self):
        # prueba que el index redirige a hello
        response= self.client.get(url_for('index'))

        self.assertRedirects(response, url_for('hello'))

    def test_hello_required(self):
        # prueba que http es 200 cuando se hace un get
        response= self.client.get(url_for('hello'))
        self.assertEquals(response.status_code, 302)
    
    def test_hello_post(self):
        # prueba para un post
        response= self.client.post(url_for('hello'))

        self.assertTrue(response.status_code, 405)
    
    def test_auth_blueprint_exists(self):
        self.assertIn('auth', self.app.blueprints)

    def test_auth_login_get(self):
        response= self.client.get(url_for('auth.login'))

        self.assert200(response)

    def test_auth_login_template(self):
        # para ver que se rendereo el template
        self.client.get(url_for('auth.login'))
        self.assertTemplateUsed('login.html')
    
    def test_auth_login_post(self):
        # prueba para un post
        fake_form= {'username': 'emmanuel', 'password': '12345678'}
        response= self.client.post(url_for('auth.login'), data= fake_form)
        self.assertRedirects(response, url_for('auth.signup'))
        response= self.client.get(url_for('hello'))
        self.assertEquals(response.status_code, 302)

    def test_app_database_exists(self):
        self.assertIsNotNone(db)
    
    def test_auth_signup_get(self):
        # prueba que http es 200 cuando se hace un get
        response= self.client.get(url_for('auth.signup'))
        
        self.assert200(response)