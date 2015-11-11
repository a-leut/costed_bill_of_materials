import pandas as pd
from os import path
from project.models import Cbom, CbomRow
from project import db

def import_cbom(file):
    create_cbom_record(file)

def create_cbom_record(file):
    filename = path.basename(file)
    c = Cbom(name=filename)
    db.session.add(c)
    db.session.commit()

import_cbom('bom.xls')