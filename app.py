from flask import Flask, render_template, flash, request, redirect, url_for, session, logging, request
from wtforms import Form, StringField , TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

# pip install Flask-WTF
# pip install passlib

app = Flask(__name__) # object called app is created of Flask class

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
	username = StringField('Username',[validators.Length(min = 4, max = 25)])
	email = StringField('Email',[validators.Length(min = 6, max = 50)])
	password = PasswordField('Password',[
		validators.DataRequired(),
		validators.EqualTo('confirm',message = 'Passwords do not match')
		])
	confirm = PasswordField('Confirm Password')


@app.route('/signup',methods=['GET','POST'])
def signup():
	form = Signup(request.form)
	if request.method == 'POST' and form.validate():
		name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))
        
	return render_template('signup.html',form = form)

if __name__ == '__main__':
	app.secret_key = 'secretZone'
	app.run(debug = True)
