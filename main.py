import os
from flask import app, request, redirect, make_response, render_template, session, url_for, flash
import unittest
from app import create_app
from app.forms import TodoForm, DeleteTodoForm, UpdateTodoForm
from app.models import db, Users, Todos, get_id_user
from flask_login import login_required, current_user


app = create_app()


# configurando flask-testing
@app.cli.command()
def test():
    # cargar y correr todos los test del directorio test
    test= unittest.TestLoader().discover('tests')  
    unittest.TextTestRunner().run(test)


# configurando paginas de error 404
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error= error)

# create the ddbb if it does not exist
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    user_ip= request.remote_addr
    response= make_response(redirect('/hello'))
    session['user_ip']= user_ip
    return response


@app.route('/hello', methods= ['GET', 'POST'])
@login_required
def hello():
    user_ip= session.get('user_ip')   
    username= current_user.id
    id_user= get_id_user(username)
    todos_user= Todos.query.filter_by(id_user= id_user).all()
    todo_form= TodoForm()
    delete_form= DeleteTodoForm()
    update_form= UpdateTodoForm()

    context= {
        'user_ip': user_ip,
        'id_user': id_user,
        'todos': todos_user,
        'username': username,
        'todo_form': todo_form,
        'delete_form': delete_form,
        'update_form': update_form,
    }
    if todo_form.validate_on_submit():
        description= todo_form.description.data
        new_todo= Todos(description=description, done= False, id_user=id_user)

        db.session.add(new_todo)
        db.session.commit()
        flash('Tareada creada con exito!')
        return redirect(url_for('hello'))

    return render_template('hello.html', **context)


@app.route('/todos/delete/<todo_id>', methods= ['POST'])
def delete(todo_id):
    todo_delete= Todos.query.filter_by(todo_id= todo_id).first()

    if todo_delete is not None:
        db.session.delete(todo_delete)
        db.session.commit()
        flash('Tarea eliminada', 'success')
        return redirect(url_for('hello'))

@app.route('/todos/update/<todo_id>', methods= ['POST'])
def update(todo_id):
    #arriba en route /<int:done>
    todo_update= Todos.query.filter_by(todo_id= todo_id).first()

    if todo_update.done == 0:
        todo_update.done = 1
    else:
        todo_update.done = 0
    
    db.session.commit()
    flash('Se ha cambiado el estado de la Tarea')
    return redirect(url_for('hello'))


if __name__ == '__main__':
    app.run(port= 5000, debug= True)
    if not os.path.exists('db.sqlite'):
        db.create_all()
