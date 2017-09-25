import MySQLdb

def connection():
    conn=MySQLdb.connect(host='localhost',
            user='root',
            passwd='dec3ptious',
            db='Stock_Screener')
    c=conn.cursor()

    return c, conn
