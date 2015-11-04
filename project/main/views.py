# project/main/views.py


#################
#### imports ####
#################

from flask import render_template, Blueprint
from flask_login import login_required


################
#### config ####
################

main_blueprint = Blueprint('main', __name__,)


################
#### routes ####
################


@main_blueprint.route('/')
def home():
    return render_template('main/home.html')

@main_blueprint.route("/cbom/")
@login_required
def cbom():
    return render_template("main/about.html")
