from flask import render_template,session,redirect,flash,url_for
from flask_login import login_user,login_required,logout_user
from werkzeug.security import generate_password_hash,check_password_hash
from app.forms import LoginForm
from . import auth
from app.sql_service2 import Connection
from app.models import UserModel,UserData
import re

@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    context={
        'login_form': login_form
    }
    if login_form.validate_on_submit():
        username=login_form.username.data
        password = login_form.password.data
        #session['username']=username

        user_doc = Connection.get_userc(connection=Connection.connection,user_id=username)

        if user_doc is not None:
            if check_password_hash(((user_doc[0])['password']),password): #password_from_db = ((user_doc[0])['password'])
            #if password == password_from_db:    
                user_data = UserData(username,password)
                user=UserModel(user_data)            

                login_user(user)

                flash('Bienvenido de Nuevo!')

                redirect(url_for('hello'))
            else:
                flash('La información no coincide')
        else:
            flash('El usuario no existe')
                

        #flash('Nombre de usuario '+ username + ' registrado con exito!')

        return redirect(url_for('index'))
    return render_template('login.html',**context)


@auth.route('signup',methods=['GET','POST'])
def signup():
    signup_form = LoginForm()
    context ={
        'signup_form': signup_form
    }

    if signup_form.validate_on_submit():
        username =signup_form.username.data
        password = signup_form.password.data

        if re.match("^[a-zA-Z0-9_]*$",username):

            user_doc = Connection.get_userc(connection=Connection.connection,user_id=username)#Connection.get_userc(connection=Connection.connection,user_id='username')

            if user_doc is None:
                password_hash = generate_password_hash(password)
                user_data = UserData(username,password_hash)
                Connection.user_put(user_data,Connection.connection)

                user = UserModel(user_data)

                login_user(user)

                flash('Bienvenido nuevo usuario')

                return redirect(url_for('hello'))
            
            else:
                flash(f'el usuario {username.title()} ya existe')
        else:
            flash(f'¡El usuario {username} que intentas crear no puede contener espacios ni caracteres especiales!')

    return render_template('signup.html',**context)

@auth.route('logout')
@login_required
def logout():
    logout_user()
    flash('Regresa pronto')

    return redirect(url_for('auth.login'))




