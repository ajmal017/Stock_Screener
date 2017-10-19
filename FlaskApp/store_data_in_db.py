import MySQLdb
import dbconnect
import pandas as pd

c, conn = dbconnect.connection()
DIR = 'C:/Users/Rajesh Rao/version_control/Stock_Screener_Data/'
DIR1 = 'C:/Users/Rajesh Rao/version_control/Stock_Screener_Data/Fundamental_Data/Edited/Blah/'
names = pd.read_csv(DIR+'output.csv')
name = names['Name'][0]
# print(name)
for name in names['Name']:
    c.execute("LOAD DATA LOCAL INFILE "+"'"+DIR1+name+".csv"+"'" + " INTO TABLE " name".csv"+" FIELDS TERMINATED BY ',' ENCLOSED BY '\"' LINES TERMINATED BY '\n' IGNORE 1 LINES")
    # c.execute("CREATE TABLE YOYO (name VARCHAR(10));")
    break
