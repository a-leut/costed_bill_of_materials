# project/models.py

from project import db


class Cbom(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(265), nullable=False)
    rows = db.relationship('CbomRow', backref='cbom', lazy='dynamic')

class CbomRow(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cbom_id = db.Column(db.Integer, db.ForeignKey('cbom.id'))
    cpn = db.Column(db.String(50))
    mpn = db.Column(db.String(50))
    man_name = db.Column(db.String(100))
    description = db.Column(db.String(255))
    unit_price = db.Column(db.Numeric)
    quantity = db.Column(db.Integer)
