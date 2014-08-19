# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask.ext.login import login_required
from flask.ext.httpauth import HTTPBasicAuth

#from appname import cache
#from appname.forms import LoginForm
#from appname.models import User

main = Blueprint('main', __name__)

@main.route('/')
#@cache.cached(timeout=1000)
def home():
    return render_template('empty.html')


@main.route("/logout")
def logout():
    logout_user()
    flash("You have been logged out.", "success")

    return redirect(url_for(".home"))


@main.route("/restricted")
@login_required
def restricted():
    return "You can only see this if you are logged in!", 200
