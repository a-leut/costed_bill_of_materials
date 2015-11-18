import pandas as pd
from os import path
from project.models import Cbom, CbomRow
from project import db

def import_cbom(file, filename):
    cbom = create_cbom_record(filename)
    create_cbom_row_records(file, cbom)

def create_cbom_record(filename):
    print('heres the filename: ', filename)
    c = Cbom(name=filename)
    db.session.add(c)
    db.session.commit()
    return c

def create_cbom_row_records(file, cbom):
    df = pd.read_excel(file)
    print(df.columns.values)
    for row in df.iterrows():
        cbom_row = CbomRow()
        cbom_row.cbom_id = cbom.id
        cbom_row.upload_date = cbom.upload_date
        print(row[1])
        cbom_row.cpn = row[1]['Customer Part Number']
        cbom_row.description = row[1]['Description']
        cbom_row.quantity = row[1]['QTY']
        cbom_row.MOQ = row[1]['MOQ']
        cbom_row.man_name = row[1]['Manufacturer']
        cbom_row.mpn = row[1]['MPN']
        cbom_row.unit_price = row[1]['Unit Price']
        db.session.add(cbom_row)
    db.session.commit()
