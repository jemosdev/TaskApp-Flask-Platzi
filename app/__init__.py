# aca se realizaran las configuraciones iniciales para la creacion de la app
# se registra el modulo auth como blueprint, toma configuraciones para la sesion y del usuario una vez loggeado
from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Config
from .auth import auth
from flask_login import LoginManager
from .models import db, UserModel


login_manager= LoginManager()
login_manager.login_view= 'auth.login'

#obtener el usuario directamente de la ddbb usa el metodo query en models
@login_manager.user_loader          
def load_user(username):
    return UserModel.query(username)

def create_app():
    # nos va a regresar a la nueva aplicacion
    app = Flask(__name__)
    bootstrap= Bootstrap(app)
    
    app.config.from_object(Config)
    
    db.init_app(app)
    
    login_manager.init_app(app)
    
    app.register_blueprint(auth)
    
    return app
