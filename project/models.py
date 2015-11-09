# project/models.py

from project import db


class Cbom(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(265), unique=True, nullable=False)
    rows = db.relationship('CbomRow',backref='cbom',lazy='dynamic')

class CbomRow(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cbom_id = db.Column(db.Integer, db.ForeignKey('cbom.id'))
    man_part_num = db.Column(db.String(50))
    int_part_num = db.Column(db.String(50))
    unit_price = db.Column(db.Numeric)
    quantity = db.Column(db.Integer)
