import dbconnect
import pandas as pd
COMP_NAMES = '../../Stock_Screener_Data/output.csv'
SQL_NAME = '../../Stock_Screener_Data/output_sql.csv'
DATA = '../../Stock_Screener_Data/Fundamental_Data/'
c,conn=dbconnect.connection()
NSE=pd.read_csv(COMP_NAMES)['Name'].values
NSE1 = pd.read_csv(SQL_NAME)['Name'].values
for comp, comp1 in zip(NSE, NSE1):
    # comp_data = pd.read_csv(DATA+comp+'.csv')
    comp_data_path = DATA+comp+'.csv'
    print(comp)
    c.execute("LOAD DATA LOCAL INFILE '%s' INTO TABLE %s_F FIELDS TERMINATED BY ',' ENCLOSED BY '\"' LINES TERMINATED BY '\r\n' IGNORE 1 LINES;"%(comp_data_path, comp1))
    conn.commit()
    # for index,row in comp_data.iterrows():
    #     try:
    #         # c.execute("INSERT INTO %s_F () values('%s',%s,%s,%s,%s,%s,%s,%s);"%(comp,row['Date'],row['Open'],row['High'],row['Low'],row['Last'],row['Close'],row['Total Trade Quantity'],row['Turnover (Lacs)']))
    #         c.execute("INSERT INTO %s_F () values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);" %(comp1, row.ix[0,0], row['Sales'], row['Depreciation'], row['Interest'], row['Profit_before_tax'], row['Tax'], row['Net_profit'], row['Dividend_Amount'], row['Equity_Share_Capital'], row['Reserves'], row['Borrowings'], row['Other_Liabilities'], row['Net_Block'], row['Capital_Work_in_Progress'], row['Investments'], row['Other_Assets'], row['Receivables'], row['Inventory'], row['Cash_and_Bank'], row['No_of_Equity_Shares']))
    #
    #         conn.commit()
    #     except:
    #         pass
