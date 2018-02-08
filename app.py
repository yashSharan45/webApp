from flask import Flask, render_template, flash, request, redirect, url_for, session, logging, request
from wtforms import Form, StringField , TextAreaField, PasswordField, validators
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt

# pip install Flask-WTF
# pip install passlib

app = Flask(__name__) # object called app is created of Flask class

#Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'toor'
app.config['MYSQL_DB'] = 'portalDB'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

#init MYSQL
mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

# USING WTFORMS MAKING A FORM CLASS WITH INBUILT VALIDATIONS
class Signup(Form):
    name = StringField('Name',[validators.Length(min = 1, max = 50)])
    email = StringField('Email',[validators.Length(min = 6, max = 50)])
    username = StringField('Username',[validators.Length(min = 4, max = 25)])
    password = PasswordField('Password',[
        validators.DataRequired(),
        validators.EqualTo('confirm',message = 'Passwords do not match')
        ])
    confirm = PasswordField('Confirm Password')

# signup for user
@app.route('/signup',methods=['GET','POST'])
def signup():
    form = Signup(request.form)    
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        #Create Cursor
        cur = mysql.connection.cursor()
        
        #Execute Cursor
        cur.execute("INSERT INTO UserDB(Name,Email,Username,Password) VALUES (%s,%s,%s,%s)",(name,email,username,password))
        #cur.execute("INSERT INTO temp(Name,Email,Username,Password) VALUES (%s,%s,%s,%s)",(name,email,username,password))

        
        #Commit to DB
        mysql.connection.commit()

        #Close Connection
        cur.close()

        flash('You are now registered and can log in','success')
        return render_template('home.html')
        #return redirect(url_for('home'))

    return render_template('signup.html', form = form)

class SignupCompany(Form):
    name = StringField('Name',[validators.Length(min = 1, max = 50)])
    company_name = StringField('Company',[validators.Length(min = 1, max = 50)])
    website = StringField('Website',[validators.Length(min = 1, max = 50)])
    username = StringField('Username',[validators.Length(min = 4, max = 25)])
    email = StringField('Email',[validators.Length(min = 6, max = 50)])
    password = PasswordField('Password',[
        validators.DataRequired(),
        validators.EqualTo('confirm',message = 'Passwords do not match')
        ])
    confirm = PasswordField('Confirm Password')

# signup for company
@app.route('/signup_company',methods=['GET','POST'])
def signup_company():
    form = SignupCompany(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        company = form.company_name.data
        website = form.website.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        #Create Cursor
        cur = mysql.connection.cursor()
        
        #Execute Cursor
        cur.execute("INSERT INTO CompanyDB(Name,Company,Website,Email,Username,Password) VALUES (%s,%s,%s,%s,%s,%s)",(name,company,website,email,username,password))
        #cur.execute("INSERT INTO temp(Name,Email,Username,Password) VALUES (%s,%s,%s,%s)",(name,email,username,password))

        
        #Commit to DB
        mysql.connection.commit()

        #Close Connection
        cur.close()

        flash('You are now registered and can log in','success')
        return render_template('home.html')
        #return redirect(url_for('home'))
    return render_template('signup_company.html',form = form)

if __name__ == '__main__':
    app.secret_key = 'secretZone'
app.run(debug = True)