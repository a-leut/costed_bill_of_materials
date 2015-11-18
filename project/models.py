# project/models.py

from project import db
from sqlalchemy import UniqueConstraint
import datetime

class Cbom(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(265), nullable=False)
    upload_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    rows = db.relationship('CbomRow', backref='cbom', lazy='dynamic')
    UniqueConstraint('upload_date', 'name', name='uix_1')

class CbomRow(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cbom_id = db.Column(db.Integer, db.ForeignKey('cbom.id'))
    cpn = db.Column(db.String(50))
    mpn = db.Column(db.String(50))
    man_name = db.Column(db.String(100))
    description = db.Column(db.String(255))
    upload_date = db.Column(db.DateTime)
    unit_price = db.Column(db.Numeric)
    total_price = db.Column(db.Numeric)
    quantity = db.Column(db.Integer)
    MOQ = db.Column(db.Integer)
    new_cool_columns = db.Column(db.String(10))
