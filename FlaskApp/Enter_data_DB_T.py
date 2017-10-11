import dbconnect
import pandas as pd


c,conn=dbconnect.connection()
NSE=pd.read_csv('nifty200.csv')['Symbol'].values
compdata=pd.read_csv('../../data/ACC.csv')
for row in compdata.iterrows():
    print(row)
'''
for comp in NSE:
    compdata=pd.read_csv('../../data/'+str(comp)+'.csv')
    print(list(compdata))
'''  


