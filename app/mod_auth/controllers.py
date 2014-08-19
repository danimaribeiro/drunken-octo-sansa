'''
Created on 19/08/2014

@author: danimaribeiro
'''
# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash,  session, redirect, url_for
from flask.ext.login import login_user, logout_user

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

# Import module forms
from app.mod_auth.forms import LoginForm, RegistroForm
from app import mongo

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

# Set the route and accepted methods
@mod_auth.route('/login/', methods=['GET', 'POST'])
def login():

    # If sign in form is submitted
    form = LoginForm(request.form)
    # Verify the sign in form
    if form.validate_on_submit():
        user = mongo.db.users.find_one({'email': form.email.data, 'senha': form.password.data})
        if user:
            iden = user['_id']
            login_user(str(iden))
            flash('Welcome %s' % user['nome'])
            return redirect(url_for('main.home'))

        flash('Usuário ou senha inválidos', 'error-message')

    return render_template("auth/login.html", form=form)


@mod_auth.route('/signin/', methods=['GET', 'POST'])
def signin():
    form = RegistroForm(request.form)
    if form.validate_on_submit():
        novo = { "nome": form.nome.data, "email": form.email.data, "senha": form.senha.data }
        mongo.db.users.save(novo)

        return redirect(url_for('auth.login'))

    return render_template("auth/signin.html", form=form)

@mod_auth.route('/recuperar/', methods=['GET', 'POST'])
def recuperar():
    form = RegistroForm(request.form)
    return render_template("auth/recuperar.html", form=form)

