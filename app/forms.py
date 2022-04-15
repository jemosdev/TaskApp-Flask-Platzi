from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


# creando una forma ingresar y/o registrar usuario
class LoginForm(FlaskForm):
    username= StringField('Nombre de usuario:', validators= [DataRequired()])
    password= PasswordField('Password', validators= [DataRequired()])
    submit= SubmitField('Enviar')

# creando una forma para crear tarea
class TodoForm(FlaskForm):
    description= StringField('Descripcion:', validators= [DataRequired()])
    submit= SubmitField('Crear')

# creando una forma borrar tarea
class DeleteTodoForm(FlaskForm):
    submit= SubmitField('Borrar')

# creando una forma para modificar
class UpdateTodoForm(FlaskForm):
    submit= SubmitField('Tarea Completada')