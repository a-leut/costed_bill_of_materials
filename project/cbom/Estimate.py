import pandas as pd
from os import path
from project.models import Cbom, CbomRow
from project import db

def Estimate(BOM)
    df = pd.read_excel(BOM)
    for row in df.iterrows():
        if(row[1]["Manufacturer Part"] != None):
                row['Unit Price'] = CbomRow.query.filter(row[1]["Manufacturer Part"]).order_by(CbomRow.upload_date).unit_price
        elif(row[1]["Customer Part Number"] != None):
                row['Unit Price'] = CbomRow.query.filter(row[1]["Customer Part Number"]).order_by(CbomRow.upload_date).unit_price
    #somehow set this to the user desktop.
