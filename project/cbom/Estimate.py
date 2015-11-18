import pandas as pd
import numpy as np
from project.models import CbomRow

def estimate_bom(bom):
    df = pd.read_excel(bom)
    print(df)
    df["Unit Price"] = df.apply(estimate_row, axis=1)
    df["MOQ"] = df.apply(estimate_row_MOQ, axis=1)
    return df

def estimate_row(row):
    """
    :param row: Row in dataframe with mpn and cpn column
    :return: Price of record matching on mpn or cpn if it exists
    """
    # first lookup by mpn
    mpn = row["Manufacturer Part"]
    rec = CbomRow.query.filter(CbomRow.mpn == mpn).\
        order_by(CbomRow.upload_date).first()
    if rec:
        return rec.unit_price
    else:
        # otherwise lookup by cpn
        cpn = row["Customer Part Number"]
        rec = CbomRow.query.filter(CbomRow.cpn == cpn).\
            order_by(CbomRow.upload_date).first()
        if rec:
            return rec.unit_price
        else:
            return 0
def estimate_row_MOQ(row):
    """
    :param row: Row in dataframe with mpn and cpn column
    :return: Price of record matching on mpn or cpn if it exists
    """
    # first lookup by mpn
    mpn = row["Manufacturer Part"]
    rec = CbomRow.query.filter(CbomRow.mpn == mpn).\
        order_by(CbomRow.upload_date).first()
    if rec:
        return rec.MOQ
    else:
        # otherwise lookup by cpn
        cpn = row["Customer Part Number"]
        rec = CbomRow.query.filter(CbomRow.cpn == cpn).\
            order_by(CbomRow.upload_date).first()
        if rec:
            return rec.MOQ
        else:
            return 0
