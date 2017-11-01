
####################IMPORTANT SHIT##############################################
'''
PROCEDURE FOR AVERAGE VALUE OF ANY COLUMN
PROCEDURE FOR SUM OF ANY COLUMN
Procedure for ROE
PROCEDURE FOR BOOK VALUE

TO_RUN:
delimiter //
DROP PROCEDURE avg_val//
CREATE PROCEDURE avg_val(comp_name varchar(20), field_name varchar(30), out output float)
BEGIN
    set @comp_name = comp_name;
    set @field_name = field_name;
    set @r = 0.0;
    call average_value(@comp_name, @field_name, 1, @r);
    set output = @r;
END//
DROP PROCEDURE sum_val//
CREATE PROCEDURE sum_val(comp_name varchar(20), field_name varchar(30), out output float)
BEGIN
    set @comp_name = comp_name;
    set @field_name = field_name;
    set @r = 0.0;
    call sum_value(@comp_name, @field_name, 1, @r);
    set output = @r;
END//
delimiter ;


DROP PROCEDURE average_value//
CREATE PROCEDURE average_value(comp_name varchar(20), field_name varchar(30), years int, out output float)
BEGIN
    set @comp_name = comp_name;
    set @field_name = field_name;
    set @sql_text = concat('select avg(',@field_name,') into @outp from (select ',@field_name,' from nse200_F where Comp_ID = "',comp_name,'" order by Year DESC limit ',years,') as gg');
    prepare stmt1 from @sql_text;
    execute stmt1;
    set output = @outp;
    deallocate prepare stmt1;
END//
DROP PROCEDURE sum_value//
CREATE PROCEDURE sum_value(comp_name varchar(20), field_name varchar(30), years int, out output float)
BEGIN
    set @comp_name = comp_name;
    set @field_name = field_name;
    set @sql_text = concat('select sum(',@field_name,') into @outp from (select ',@field_name,' from nse200_F where Comp_ID = "',comp_name,'" order by Year DESC limit ',years,') as gg');    prepare stmt1 from @sql_text;
    execute stmt1;
    set output = @outp;
    deallocate prepare stmt1;
END//
DROP PROCEDURE roe//
CREATE PROCEDURE roe(comp_name varchar(20), years int, out output float)
BEGIN
    set @comp_name = comp_name;
    set @r = 0.0;
    set @e = 0.0;
    call sum_value(@comp_name, "Net_profit", years, @r);
    call sum_value(@comp_name, "Reserves", years, @e);
    set output = @r*100/@e;
END//
DROP PROCEDURE average_book_value//
CREATE PROCEDURE average_book_value(comp_name varchar(20), years int, out output float)
BEGIN
    set @comp_name = comp_name;
    set @b = 0.0;
    set @v = 0.0;
    call sum_value(@comp_name, "No_of_Equity_Shares", years, @e);
    call sum_value(@comp_name, "Reserves", years, @b);
    set output = @r*100/@e;
END//
delimiter ;



em discography
https://mega.nz/#F!tpF1DbYb!nWq6t_lethGSQLwnM9oExg
'''
########################################################################################


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

TODO
1. paste fundamental_data in right folder
2. past niftyind and output in right folder
3. run store_data and populate_data
4. run all procs in mysql
5. check if works in init
6. add procs for pe and pb
7. add procs for moving avgs and adx
8. do report
