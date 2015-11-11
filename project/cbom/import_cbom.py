import pandas as pd
from os import path
from project.models import Cbom, CbomRow
from project import db

def import_cbom(file):
    cbom = create_cbom_record(file)
    create_cbom_row_records(file, cbom)

def create_cbom_record(file):
    filename = path.basename(file)
    c = Cbom(name=filename)
    db.session.add(c)
    db.session.commit()
    return c

def create_cbom_row_records(file, cbom):
    df = pd.read_excel(file)
    for row in df.iteritems():
        print('on a row:', row)

import_cbom('bom.xls')