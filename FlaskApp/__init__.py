from flask import Flask, render_template,flash,request,url_for,redirect,session
from content_management import Content
from dbconnect import connection
from wtforms import Form
from passlib.hash import sha256_crypt
from MySQLdb import escape_string as thwart
import gc

app = Flask(__name__)

@app.route('/')
def homepage():
    return "Stock Screener"

class RegistrationForm(Form):
    username=TextField('Username',[validators.Length(min=4,max=20)])
    email=TextField('Email Address',[validators.Length(min=6,max=50)])
    password=PasswordField('Password',[validators.Required(),
        validators.EqualTo('confirm',message="Passwords must Match")]) 
    confirm= PasswordField('Repeat password')
    accept_tos=BoolenField('GG')
    
@app.route('/register/',methods=['GET','POST'])
def register_page():
    try:
        form=RegistrationForm(request.form)
        if request.method=="POST" and form.validate():
            username=form.username.data
            email=form.email.data
            password=sha256_crypt.encrypt((str(form.password.data)))
            c,conn =connection()
            x=c.execute("select * from users where username=(%s)",
                    (thwart(username)))

            if int(x) >0:
                flash("Username taken boi")
                return render_template('register.html',form=form)
            else:
                c.execute("insert into users (username,password,email) values(%s,%s,%s)"
                (thwart(username),thwart(password),thwart(email)))
                conn.commit()
                flash("thanks for registering")
                c.close()
                conn.close()
                gc.collect()
                session['logged_in']=True
                session['username']=username
                return redirect(url_for('dashboard'))

            return render_template("register.html",form=form)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run()
