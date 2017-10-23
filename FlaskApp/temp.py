from dbconnect import connection
comp = "TATAMOTORS"
c,conn=connection()
query = "SELECT * FROM %s_F ;"%(comp)
c.execute(query)
data = c.fetchall()
print(data)
