# project/__init__.py


#################
#### imports ####
#################

import os
from flask import Flask, render_template
from flask_login import LoginManager
from flask_debugtoolbar import DebugToolbarExtension
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from project.config import DevelopmentConfig

# fix for pyinstaller
import flask_bootstrap as _

################
#### config ####
################

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

####################
#### extensions ####
####################

login_manager = LoginManager()
login_manager.init_app(app)
toolbar = DebugToolbarExtension(app)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

###################
### blueprints ####
###################

from project.cbom.views import main_blueprint
app.register_blueprint(main_blueprint)

########################
#### error handlers ####
########################

@app.errorhandler(403)
def forbidden_page(error):
    return render_template("errors/403.html"), 403


@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"), 404


@app.errorhandler(500)
def server_error_page(error):
    return render_template("errors/500.html"), 500
