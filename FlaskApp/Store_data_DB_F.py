import dbconnect
import pandas as pd


c,conn=dbconnect.connection()
NSE=pd.read_csv('nifty200.csv')['Symbol'].values
for comp in NSE:
    c.execute("CREATE TABLE %s_F (Date DATE PRIMARY KEY, Sales FLOAT, RawMAT FLOAT, Cinv FLOAT, PandF FLOAT, Othermfr FLOAT, EMPC FLOAT, sanda FLOAT ,othrexp FLOAT,othrinc FLOAT,DEP FLOAT,INTR FLOAT,PBT FLOAT,Tax FLOAT,);"%str(comp))



