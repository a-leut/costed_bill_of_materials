# project/main/views.py


#################
#### imports ####
#################

from flask import render_template, Blueprint, send_file
from flask import flash, request
from .forms import CbomUploadForm, CbomSearchForm, PartSearchForm
from project.models import Cbom, CbomRow
from io import BytesIO, StringIO
from project.cbom.import_cbom import import_cbom
from project.cbom.estimate import estimate_bom
import pandas as pd


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
        file = request.files[form.file.data.name].read()
        filename = request.files[form.file.data.name].filename
        import_cbom(BytesIO(file), filename)
        flash('Uploaded file ', filename)
    return render_template('cbom/upload.html', form=form)

@main_blueprint.route('/estimate/', methods=('GET', 'POST'))
def estimate():
    form = CbomUploadForm()
    if form.validate_on_submit():
        bom = request.files[form.file.data.name].read()
        filename = request.files[form.file.data.name].filename
        # estimate the cost of the cbom
        df = estimate_bom(BytesIO(bom))
        # create excel file in memory and return to user
        io = BytesIO()
        writer = pd.ExcelWriter('not_used.xlsx')
        writer.book.filename = io
        df.to_excel(writer, index=False)
        writer.close()
        io.seek(0)
        return send_file(io,
                         as_attachment=True,
                         attachment_filename="estimated_" + filename)

    return render_template('cbom/estimate.html', form=form)

@main_blueprint.route('/')
def home():
    return render_template('cbom/home.html')

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

@main_blueprint.route("/search_part/", methods=['GET', 'POST'])
def search_part():
    form = PartSearchForm()
    if form.validate_on_submit():
        matching_cboms = CbomRow.query.filter(CbomRow.mpn == form.filename.data).all()
        # if there are matching cboms, show user list of them to select from
        if len(matching_cboms) > 0:
            return render_template('cbom/part_list.html', cboms=matching_cboms, str=str)
        else:
            flash('No matching Parts found')
    return render_template("cbom/search_part.html", form=form)

@main_blueprint.route("/view_cbom_<id>/")
def view_cbom(id):
    CBOM = Cbom.query.filter(Cbom.id == id).first()
    cbom_rows = CbomRow.query.filter(CbomRow.cbom_id == id).all()
    return render_template("cbom/view_cbom.html/", CBOM=CBOM, rows=cbom_rows)