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
    for row in df.iterrows():
        cbom_row = CbomRow()
        cbom_row.cbom_id = cbom.id
        cbom_row.cpn = row[1][1]
        cbom_row.description = row[1][2]
        cbom_row.quantity = row[1][3]
        cbom_row.man_name = row[1][4]
        cbom_row.mpn = row[1][5]
        db.session.add(cbom_row)
    db.session.commit()

import_cbom('bom.xlsx')