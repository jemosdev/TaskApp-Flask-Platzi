from app.forms import LoginForm
from enum import auto
from . import auth
from flask import session, flash, redirect, url_for, render_template
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

from app.models import db, UserData, get_user, UserModel, Users


# declarar un nuevo view
@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form= LoginForm()
    context= {
        'login_form': login_form
    }
    if login_form.validate_on_submit():
        username= login_form.username.data
        password= login_form.password.data

        user_doc= get_user(username)
        user_id= user_doc.id

        if user_doc is not None:
            if check_password_hash(user_doc.password, password):
                user_data= UserData(username, password)
                user= UserModel(user_data)
                session['id_user']= user_id

                login_user(user)
                flash('Bienvenido de nuevo')
                redirect(url_for('hello'))
            else:
                flash('La informacion no coincide')
        else:
            flash('El usuario no existe')
            return redirect(url_for('auth.signup'))
        return redirect(url_for('index'))
        
    return render_template('login.html', **context)

# declarar un nuevo view
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Regrese pronto')

    return redirect(url_for('auth.login'))

# declarar un nuevo view
@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    signup_form= LoginForm()
    context= {
        'signup_form': signup_form
    }

    if signup_form.validate_on_submit():
        username= signup_form.username.data
        password= signup_form.password.data

        user_doc= get_user(username)
        
        #buscar el usuario en la ddbb
        user_doc= Users.query.filter_by(username=username).first()

        if user_doc:
            flash('El nombre de usuario ya existe')

            return redirect(url_for('auth.signup'))

        else:
            new_user= Users(username= username, password= generate_password_hash(password, method= 'sha256'))
            db.session.add(new_user)
            db.session.commit()
            user_data= UserData(username, password)
            #user_put(user_data)
            user= UserModel(user_data)
            login_user(user)
            flash('Bienvenido(a)')
            return redirect(url_for('hello'))
        
    return render_template('signup.html', **context)