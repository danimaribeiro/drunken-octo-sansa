# Import flask and template operators
from flask import Flask, render_template
from flask.ext.pymongo import PyMongo
from flask.ext.login import LoginManager
from flask.ext.assets import Environment
from app.assets import common_js, common_css

# Define the WSGI application object
app = Flask(__name__)
app.config['metrics_DBNAME'] = 'metrics'
mongo = PyMongo(app, config_prefix='metrics')
login_manager = LoginManager()
login_manager.init_app(app)

assets = Environment(app)
assets.register('js_all', common_js)
assets.register('css_all', common_css)

# Configurations
app.config.from_object('config')

@login_manager.user_loader
def load_user(userid):
    return mongo.db.users.find_one({ "_id": userid })

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
from app.mapas.controllers import mapa
from app.graficos.controllers import graphs

# Register blueprint(s)
app.register_blueprint(auth_module)
app.register_blueprint(main)
app.register_blueprint(mapa)
app.register_blueprint(graphs)