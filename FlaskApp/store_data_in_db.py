import MySQLdb
import dbconnect
import pandas as pd

c, conn = dbconnect.connection()
DIR = 'nifty200.csv'
names = pd.read_csv(DIR)
name = names['Symbol']
c.execute("DROP TABLE nifty200")
c.execute("CREATE TABLE nifty200 (compId INT PRIMARY KEY AUTO_INCREMENT,compname varchar(50));")
for comp in name:
    c.execute("INSERT INTO nifty200(compname) values('%s');"%(comp))
    conn.commit()
