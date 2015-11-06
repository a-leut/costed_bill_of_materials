# project/main/views.py


#################
#### imports ####
#################

from flask import render_template, Blueprint
from flask_login import login_required
from flask import flash
from .forms import CbomSearchForm


################
#### config ####
################

main_blueprint = Blueprint('cbom', __name__,)


################
#### routes ####
################


@main_blueprint.route('/')
def home():
    return render_template('cbom/home.html')

@main_blueprint.route("/cbom/")
@login_required
def cbom():
    return render_template("cbom/about.html")

@main_blueprint.route("/search_cbom/", methods=['GET', 'POST'])
@login_required
def search_cbom():
    form = CbomSearchForm()
    if form.validate_on_submit():
        flash('we searched')
    return render_template("cbom/search_cbom.html", form=form)

