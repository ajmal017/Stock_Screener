import dbconnect
import pandas as pd


c,conn=dbconnect.connection()
NSE=pd.read_csv('nifty200.csv')['Symbol'].values
for comp in NSE:
    c.execute("CREATE TABLE %s_T (Date DATE PRIMARY KEY, Open FLOAT, High FLOAT, Low FLOAT, Last FLOAT, Close FLOAT, Qty FLOAT, TurnOver FLOAT);"%str(comp))



