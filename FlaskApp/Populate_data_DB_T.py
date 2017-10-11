import dbconnect
import pandas as pd

c,conn=dbconnect.connection()
NSE=pd.read_csv('nifty200.csv')['Symbol'].values
for comp in NSE:
    print(comp)
    comp_data=pd.read_csv('../../data/'+comp+'.csv')
    for index,row in comp_data.iterrows():
        try:
            c.execute("INSERT INTO %s_T (Date,Open,High,Low,Last,Close,Qty,TurnOver) values('%s',%s,%s,%s,%s,%s,%s,%s);"%(comp,row['Date'],row['Open'],row['High'],row['Low'],row['Last'],row['Close'],row['Total Trade Quantity'],row['Turnover (Lacs)']))
            conn.commit()
        except:
            pass
