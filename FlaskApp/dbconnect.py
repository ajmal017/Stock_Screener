import MySQLdb

def connection():
    conn=MySQLdb.connect(host='localhost',
            user='root',
            #passwd='bakra123',
            passwd='dec3ptious',
            db='Stock_Screener')
    c=conn.cursor()
    print("DONE")

    return c, conn
