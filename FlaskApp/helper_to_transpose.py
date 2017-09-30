import MySQLdb
import dbconnect
import pandas as pd

c, conn = dbconnect.connection()
DIR = 'C:/Users/Rajesh Rao/version_control/Stock_Screener_Data/'
DIR1 = 'C:/Users/Rajesh Rao/version_control/Stock_Screener_Data/Fundamental_Data/Edited/Blah/'
names = pd.read_csv(DIR+'output.csv')
name = names['Name'][0]
# print(name)
data = pd.read_csv(DIR1+name+'.csv', index_col = False)
# data.drop('42')
data = data.transpose()
data.to_csv('C:/Users/Rajesh Rao/version_control/Stock_Screener_Data/blah.csv')

for name in names['Name']:
    # c.execute("CREATE TABLE {}")
    data = pd.read_csv(DIR1+name+'.csv', index_col = False)
    # data.drop('42')
    data = data.transpose()
    data.to_csv('C:/Users/Rajesh Rao/version_control/Stock_Screener_Data/Fundamental_Data/Edited/Blah/'+name+'.csv')
