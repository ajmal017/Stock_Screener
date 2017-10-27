# import dbconnect
# '''
# Price/Earnings
# Price/Book
# Book Value
# ROE
# ROE 3 yr
# ROE 5 yr
# PAT 1 yr Growth
# PAT 3 yr Growth
# PAT 5 yr growth
#
# c,conn=connection()
# c.execute("select compname from nifty200")
# companies = c.fetchall()
# for comp in companies:
#     c.callproc('')
#
#
# QUERY = "PRICE/BOOK > 1 AND PRICE/EARNINGS > 30 AND ROE > 30"
# CHUNKS = QUERY.split("AND")
# for chunk in CHUNKS:
#     chunk = chunk.lstrip()
#     chunk = chunk.split(" ")
#     print("PARAMETER {} SIGN {} VALUE {}".format(chunk[0], chunk[1], chunk[2]))
#
# CREATE PROCEDURE price/earnings(in comp_name varchar(20))
# BEGIN
#     PREPARE stmt0 FROM 'select tec.Close into @price from (select(concat(?,"_t"))) as tec limit 1';
#     set @a = comp_name;
#     EXECUTE stmt0 USING @a;
#     PREPARE stmt FROM 'select @price/fun.Net_profit*10000000/fun.No_of_Equity_Shares as value from (select concat(?,"_f"))
#
# c.execute("select comp_name")
#
# ####################IMPORTANT SHIT##############################################
# '''
# PROCEDURE FOR AVERAGE VALUE OF ANY COLUMN
#
# CREATE PROCEDURE average_value(comp_name varchar(20), field_name varchar(30), years int)
# BEGIN
#     set @comp_name = comp_name;
#     set @field_name = field_name;
#     set @sql_text = concat('select avg(',@field_name,') from (select ',@field_name,' from ',@comp_name,'_f order by Year DESC limit ',years,') as gg');
#     prepare stmt1 from @sql_text;
#     execute stmt1;
#     deallocate prepare stmt1;
# END
#
# PROCEDURE FOR SUM OF ANY COLUMN
#
# CREATE PROCEDURE sum_value(comp_name varchar(20), field_name varchar(30), years int, out output float)
# BEGIN
#     set @comp_name = comp_name;
#     set @field_name = field_name;
#     set @sql_text = concat('select sum(',@field_name,') into @outp from (select ',@field_name,' from ',@comp_name,'_f order by Year DESC limit ',years,') as gg');    prepare stmt1 from @sql_text;
#     execute stmt1;
#     set output = @outp;
#
#     deallocate prepare stmt1;
# END
#
# Procedure for ROE
#
# CREATE PROCEDURE roe(comp_name varchar(20), years int, out output float)
# BEGIN
#     set @comp_name = comp_name;
#     set @r = 0.0;
#     set @e = 0.0;
#     call sum_value(@comp_name, "Net_profit", years, @r);
#     call sum_value(@comp_name, "Reserves", years, @e);
#     set output = @r*100/@e;
# END
#
#
# em discography
# https://mega.nz/#F!tpF1DbYb!nWq6t_lethGSQLwnM9oExg
# '''
# ########################################################################################


import dbconnect
import numpy as np
c, conn = dbconnect.connection()
c.execute("select compname from companies;")
comp_names = np.array(c.fetchall())
chunk = ["roe3", ">", "30"]
ans = []
for comp in comp_names:
    procname =  chunk[0][:-1]
    args = [comp[0], int(chunk[0][-1]), 0.0]
    output = c.callproc(procname, args)
    c.execute('select @_'+procname+'_0, @_'+procname+'_1, @_'+procname+'_2')
    temp = c.fetchall()[0]
    if (eval(str(temp[2])+chunk[1]+chunk[2])):
        ans.append(temp)
    c.close()
    c = conn.cursor()
print(ans)


# # create procedure bla(comp_name varchar(20))
# # BEGIN
# #     set @comp_name = comp_name;
# #     set @sql_text = concat('select * from ',@comp_name,'_f limit 1');
# #     prepare stmt from @sql_text;
# #     execute stmt;
# # END
