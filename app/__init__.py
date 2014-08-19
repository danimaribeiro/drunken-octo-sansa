# Import flask and template operators
from flask import Flask, render_template
from flask.ext.pymongo import PyMongo

# Define the WSGI application object
app = Flask(__name__)
mongo = PyMongo(app)

# Configurations
app.config.from_object('config')

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('500.html'), 500


# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_auth.controllers import mod_auth as auth_module
from app.controllers.main import main


# Register blueprint(s)
app.register_blueprint(auth_module)
app.register_blueprint(main)
