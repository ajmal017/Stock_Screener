from flask import Flask, render_template, flash, request, redirect, url_for, session
from content_management import content
from dbconnect import connection
import numpy as np
#from wtforms import Form
import pandas as pd
import datetime


from passlib.hash import sha256_crypt
from MySQLdb import escape_string as thwart
import gc
import scipy
import pygal

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def homepage():
    flash('test')
    if request.method=="POST":
        print("OK")
        compx=request.form['search']
        print(compx)
        #return redirect(url_for("/login
        return redirect(url_for("Technical",comp=compx))
    else:
        return render_template("main.html")

@app.route('/dashboard/')
def dashboard():
    if session["logged_in"] == True:    
        return render_template("dashboard.html")
    else:
        return redirect(url_for("login"))

@app.route('/header/', methods=['GET','POST'])
def header():
    if request.method=="POST":
        print("OK")
        compx=request.form['search']
        print(compx)
        #return redirect(url_for("/login
        return redirect(url_for("Technical",comp=compx))

    else:
        return render_template("header.html")

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method=="POST":
        c,conn=connection()
        attempted_username=request.form["username"]
        attempted_password=request.form["password"]
        data=c.execute("SELECT * FROM users WHERE username='%s';"%str(thwart(attempted_username)))
        data=c.fetchone()
        if sha256_crypt.verify(attempted_password,data):
            session["logged_in"] = True
            session["username"] = data[1]
            return redirect(url_for("dashboard"))
    return render_template("login.html")

@app.route('/register/',methods=['GET','POST'])
def register_page():
    if request.method=="POST":
        email=request.form["email"]
        username=request.form["username"]
        password=request.form["password"]
        repassword=request.form["repassword"]
        if not(password!=repassword or email==None or len(username)<3 or len(password)<3):
            password=sha256_crypt.encrypt(str(password))
            c,conn=connection()
            thwart(username)
            x=c.execute("select * from users where username='"+str(thwart(username))+"'")
            if int(x)>0:
                return render_template("register.html")
            else:
                c.execute("INSERT INTO users (username,password,email) VALUES ('%s','%s','%s');"%(str(thwart(username)),str(thwart(password)),str(thwart(email))))
                conn.commit()
                c.close()
                conn.close()
                gc.collect()
                return redirect(url_for("login"))
    return render_template("register.html")

@app.route('/Technical/<comp>/',methods=['GET','POST'])
def Technical(comp):
    try:
        c,conn=connection()
        query = "SELECT * FROM %s_F ;"%(comp)
        c.execute(query)
        data_F = c.fetchall()
        data_F=np.array(data_F)
        PL = ["Year", "Sales",	"Depr.",	"Int.",	"PBT","Tax", "NP", "Div_Amt"]
        PL_data=data_F[:,:8]
        BS=[ "Year","Eq_Share_Cap", "Reserves","Borrowings", "Oth_Liab", "Net_Block", "CWIP",	"Inv", "Oth_Assets", "Rcvbles", "Inven.", "Cash","Eq_Shares"]
        #PL_data=[a+b for a,b in zip(data_F[:][0],data_F[:][8:])]#[data_F[:,0]]#,data_F[:,8:]]
        BS_data=np.c_[data_F[:,0],data_F[:,8:]]

        # print(data)
        # return render_template("compdata.html",comp=comp,graph_data2017=graph_data2017,graph_data2016=graph_data2016,graph_data2015=graph_data2015,graph_data2014=graph_data2014, data = data)
        #return render_template("compadata.html",comp=comp, data_F = data_F, header = header)
        if request.method=="POST":
            compx=request.form['search']
            return redirect(url_for("Technical",comp=compx))
        else:
            c,conn=connection()
            c.execute("SELECT * FROM "+comp+"_T WHERE year(Date) = 2017")
            graph=pygal.Line()
            data=c.fetchall()
            date=pd.DatetimeIndex(np.array(data)[:,0])
            #print(date)
            graph.x_labels = map(lambda d: d.strftime('%Y-%m-%d'),date)
            #graph.x_labels=map(str,set(date.month))
            graph.add(comp,np.array(data)[:,1])
            graph_data2017=graph.render_data_uri()
            c.execute("SELECT * FROM "+comp+"_T WHERE year(Date) = 2016")
            graph=pygal.Line()
            data=c.fetchall()
            date=pd.DatetimeIndex(np.array(data)[:,0])
            #print(date)
            graph.x_labels = map(lambda d: d.strftime('%Y-%m-%d'),date)
            #graph.x_labels=map(str,set(date.month))
            #graph.x_labels=date.day
            graph.add(comp,np.array(data)[:,1])
            graph_data2016=graph.render_data_uri()
            c.execute("SELECT * FROM "+comp+"_T WHERE year(Date) = 2015")
            graph=pygal.Line()
            data=c.fetchall()
            date=pd.DatetimeIndex(np.array(data)[:,0])
            #print(date)
            graph.x_labels = map(lambda d: d.strftime('%Y-%m-%d'),date)
            #graph.x_labels=map(str,set(date.month))
            #graph.x_labels=date.day
            graph.add(comp,np.array(data)[:,1])
            graph_data2015=graph.render_data_uri()
            c.execute("SELECT * FROM "+comp+"_T WHERE year(Date) = 2014")
            graph=pygal.Line()
            data=c.fetchall()
            date=pd.DatetimeIndex(np.array(data)[:,0])
            #print(date)
            #graph.x_labels=date.day
            graph.x_labels = map(lambda d: d.strftime('%Y-%m-%d'),date)
            #graph.x_labels=map(str,set(date.month))
            graph.add(comp,np.array(data)[:,1])
            graph_data2014=graph.render_data_uri()
            return render_template("compdata.html",comp=comp,graph_data2017=graph_data2017,graph_data2016=graph_data2016,graph_data2015=graph_data2015,graph_data2014=graph_data2014, PL_data=PL_data,BS_data=BS_data, PL = PL,BS=BS)
    except Exception as e:
        return str(e)
        
        
    
@app.route('/screens/')
def screens():
    return render_template("screens.html")


@app.errorhandler(404)
def pagenotfound(e):
    return('404')



if __name__ == "__main__":
    app.secret_key = 'randshit'
    app.run()
