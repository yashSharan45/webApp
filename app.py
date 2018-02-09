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

@app.route('/mobile')
def mobile():
    return render_template('mobileSurvey.html')

@app.route('/admin')
def admin():
	return "Admin"


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
    	#Create Cursor
        cur = mysql.connection.cursor()

        name = form.name.data
        email = form.email.data

        #Check if Email already exists
        email_exists = cur.execute("SELECT * FROM UserDB where Email = %s",[email])
        if email_exists > 0:
        	flash('This email already exists','danger')
        
        username = form.username.data
        #Check if Username already exists
        username_exists = cur.execute("SELECT * FROM UserDB where Username = %s",[username])
        if username_exists > 0:
        	flash('This username already exists','danger')

        password = sha256_crypt.encrypt(str(form.password.data))

        
        try:
        	cur.execute("INSERT INTO UserDB(Name,Email,Username,Password) VALUES (%s,%s,%s,%s)",(name,email,username,password))
        	mysql.connection.commit()
        	cur.close()
        	flash('You are now registered and can log in','success')
        	return redirect(url_for('login'))
        except Exception as e:
        	exception_user = e
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
    	#Create Cursor
        cur = mysql.connection.cursor()

        name = form.name.data
        company = form.company_name.data
        website = form.website.data

        email = form.email.data

        #Check if Email already exists
        email_exists = cur.execute("SELECT * FROM CompanyDB where Email = %s",[email])
        if email_exists > 0:
        	flash('This email already exists','danger')

        username = form.username.data
        
        #Check if Username already exists
        username_exists = cur.execute("SELECT * FROM CompanyDB where Username = %s",[username])
        if username_exists > 0:
        	flash('This username already exists','danger')

        password = sha256_crypt.encrypt(str(form.password.data))
                
        try:
        	#Execute Cursor
            cur.execute("INSERT INTO CompanyDB(Name,Company,Website,Email,Username,Password) VALUES (%s,%s,%s,%s,%s,%s)",(name,company,website,email,username,password))
            #cur.execute("INSERT INTO temp(Name,Email,Username,Password) VALUES (%s,%s,%s,%s)",(name,email,username,password))

            #Commit to DB
            mysql.connection.commit()

            #Close Connection
            cur.close()

            flash('You are now registered and can log in','success')
            return redirect(url_for('login'))
        except Exception as e:
        	exception_company = e
    return render_template('signup_company.html',form = form)

if __name__ == '__main__':
    app.secret_key = 'secretZone'
app.run(debug = True)