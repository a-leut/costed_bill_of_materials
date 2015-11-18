# project/user/forms.py


from flask_wtf import Form
from wtforms import StringField
from flask_wtf.file import FileField

class CbomSearchForm(Form):
    filename = StringField('Partial File Name')

class PartSearchForm(Form):
    filename = StringField('Manufacturer Part Number/Customer Part Number')

class CbomUploadForm(Form):
    file = FileField('CBOMs')
