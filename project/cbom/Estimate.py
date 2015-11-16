import pandas as pd
import numpy as np
from project import db
from project.models import CbomRow

def estimate_bom(bom):
    df = pd.read_excel(bom)
    print(df)
    df["Price"]= df["Customer Part Number"].apply(cpn_lookup)
    df["Price"]= df["Manufacturer Part"].apply(mpn_lookup)
    return df

def mpn_lookup(mpn):
    rec = CbomRow.query.filter(CbomRow.mpn == mpn).order_by(CbomRow.upload_date).first()
    if rec:
        return rec.unit_price
    else:
        return 0

def cpn_lookup(cpn):
    rec = CbomRow.query.filter(CbomRow.cpn == cpn).order_by(CbomRow.upload_date).first()
    if rec:
        return rec.unit_price
    else:
        return 0