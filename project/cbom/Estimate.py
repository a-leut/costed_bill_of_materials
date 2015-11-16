import pandas as pd
import numpy as np
from project.models import CbomRow

def estimate_bom(bom):
    df = pd.read_excel(bom)
    print(df)
    # for row in df.iterrows():
    #     if(row[1]["Manufacturer Part"] != None):
    #             df.loc[1]['Unit Price'] = CbomRow.query.filter(row[1]["Manufacturer Part"]).order_by(CbomRow.upload_date).first().unit_price
    #     elif(row[1]["Customer Part Number"] != None):
    #             df.loc[1]row['Unit Price'] = CbomRow.query.filter(row[1]["Customer Part Number"]).order_by(CbomRow.upload_date).first().unit_price
    return df
