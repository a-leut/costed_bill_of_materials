# project/user/forms.py


from flask_wtf import Form
from wtforms import StringField

class CbomSearchForm(Form):
    filename = StringField('Partial File Name')