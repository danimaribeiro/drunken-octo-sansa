#coding=utf-8
from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask.ext.login import login_required
from flask.ext.httpauth import HTTPBasicAuth

#from appname import cache
#from appname.forms import LoginForm
#from appname.models import User

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')


@main.route('/nfe')
def view_nfe():
    return render_template('view_nfe.html')


@main.route("/restricted")
@login_required
def restricted():
    return "You can only see this if you are logged in!", 200
