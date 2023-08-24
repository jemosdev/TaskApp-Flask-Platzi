# Dependencias
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from flask_login import UserMixin

# creando la DDBB instanciando
db = SQLAlchemy()

class Users(db.Model):
    __tablename__= 'users'
    def __init__(self, username, password):
        self.username= username
        self.password= password
    
    id= db.Column(db.Integer, primary_key= True, autoincrement= True)
    username= db.Column(db.String(20), unique= True, nullable= False)
    password= db.Column(db.String(150), nullable= False)
    tasks= db.relationship('Todos', backref='users', lazy= True)


class Todos(db.Model):
    __tablename__= 'todos'
    def __init__(self, description, done, id_user):
        self.description= description
        self.done= done
        self.id_user= id_user
    
    todo_id= db.Column(db.Integer, primary_key= True, autoincrement= True)
    description= db.Column(db.String(50), nullable= False)
    done= db.Column(db.Boolean, nullable= False)
    id_user= db.Column(db.Integer, db.ForeignKey('users.id'), nullable= False)


def get_user(username):
    # Consultar una persona
    usuario= Users.query.filter_by(username=username).first()
    return usuario

def get_id_user(username):
    # Consultar id una persona
    active_user= get_user(username)
    return active_user.id


class UserData():
    def __init__(self, username, password):
        self.username= username
        self.password= password


class UserModel(UserMixin):
    """
    :param user_data: UserData
    """
    def __init__(self, user_data):
        self.id= user_data.username
        self.password= user_data.password
    
    @staticmethod
    def query(username):
        user_doc= get_user(username)
        user_data= UserData(
            username= user_doc.username, 
            password= user_doc.password,
        )
        
        return UserModel(user_data)
