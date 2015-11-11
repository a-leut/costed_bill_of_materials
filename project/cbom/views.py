# project/main/views.py


#################
#### imports ####
#################

from flask import render_template, Blueprint
from flask_login import login_required
from flask import flash, redirect, url_for, session, request
from .forms import CbomUploadForm, CbomSearchForm
from project.models import Cbom, CbomRow
from sqlalchemy.exc import IntegrityError
from io import BytesIO
from project.cbom.import_cbom import import_cbom
#from project.cbom.Estimate import Estimate



################
#### config ####
################

main_blueprint = Blueprint('cbom', __name__,)


################
#### routes ####
################
@main_blueprint.route('/upload/', methods=('GET', 'POST'))
def upload():
    form = CbomUploadForm()
    if form.validate_on_submit():
        # try:
        file = request.files[form.file.data.name].read()
        filename = request.files[form.file.data.name].filename
        import_cbom(BytesIO(file), filename)
        flash('Uploaded file ', filename)
        # except:
        #     flash('Error uploading file')
    return render_template('cbom/upload.html', form=form)

@main_blueprint.route('/Estimate/', methods=('GET', 'POST'))
def estimate():
    form = CbomUploadForm()
    if form.validate_on_submit():
         try:
            BOM = request.files[form.file.data.name].read()
            filename = request.files[form.file.data.name].filename
            #Estimate(BOM)
            flash('Uploaded file ', filename)
         except:
             flash('Error uploading file')
    return render_template('cbom/upload.html', form=form)

@main_blueprint.route('/')
def home():
    return render_template('cbom/home.html')

@main_blueprint.route("/cbom/")
def cbom():
    return render_template("cbom/about.html")

@main_blueprint.route("/search_cbom/", methods=['GET', 'POST'])
def search_cbom():
    form = CbomSearchForm()
    if form.validate_on_submit():
        matching_cboms = Cbom.query.filter(
            Cbom.name.like('%' + form.filename.data + '%')
        ).all()
        # if there are matching cboms, show user list of them to select from
        if len(matching_cboms) > 0:
            return render_template('cbom/list_view.html', cboms=matching_cboms, str=str)
        else:
            flash('No matching CBOMs found')
    return render_template("cbom/search_cbom.html", form=form)

@main_blueprint.route("/view_cbom_<id>/")
def view_cbom(id):
    CBOM = Cbom.query.filter(id)
    return render_template("cbom/view_cbom/", CBOM = CBOM)