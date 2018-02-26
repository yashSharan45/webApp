from exceptions import Exception
from flask import Flask, render_template, flash, request, redirect, url_for, session, logging, request
from pip._vendor.requests.compat import str
from wtforms import Form, StringField , TextAreaField, PasswordField, validators
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt
from functools import wraps
from flask_mail import Mail, Message


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

#init Mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'aneeshverma0412@gmail.com'
app.config['MAIL_PASSWORD'] = 'Chitkara@71'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail=Mail(app)




# check if user logger_in
def is_logged_in(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args,**kwargs)
		else:
			flash('Unauthorized,Please login','danger')
			return redirect(url_for('login'))
	return wrap

# a gateway of login
def is_logged_in2(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args,**kwargs)
		else:
			return redirect(url_for('login'))
	return wrap

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/index')
def index1():
    return render_template('index.html')

def send_mail(suggestions):
    app.logger.info('%s',suggestions)
    msg = Message('Message from ', sender = 'aneeshverma0412@gmail.com', recipients = ['aneesh.verma09@gmail.com'])
    msg.body = suggestions
    mail.send(msg)

# ROUTING OF PHONES
@app.route('/phones')
def phones():
    return render_template('phones.html')

@app.route('/phones/phone1')
def phone1():
    return render_template('phones/phone1.html')
@app.route('/phones/phone2')
def phone2():
    return render_template('phones/phone2.html')
@app.route('/phones/phone3')
def phone3():
    return render_template('phones/phone3.html')
@app.route('/phones/phone4')
def phone4():
    return render_template('phones/phone4.html')


# ROUTING OF LAPTOPS
@app.route('/laptops')
def laptops():
    return render_template('laptops.html')

@app.route('/laptops/mac',methods=['GET','POST'])
def lappy1():
    if request.method == 'POST':
        #sending mail from data acquired from textbox
        suggestions = request.form['text']
        send_mail(suggestions)
        # get data through invisible form
        review = request.form['starwar']
        app.logger.info('%s',review)
        
    return render_template('laptops/mac.html')
@app.route('/laptops/alienware')
def lappy2():
    return render_template('laptops/alienware.html')
@app.route('/laptops/yoga')
def lappy3():
    return render_template('laptops/yoga.html')
@app.route('/laptops/spectre')
def lappy4():
    return render_template('laptops/spectre.html')

@app.route('/lap_survey')
def survey():
    return render_template('lap_survey.html')
@app.route('/surv')
def surv():
    return render_template('surv.html')



@app.route('/web_app')
def web_app():
    return render_template('web_app.html')

@app.route('/phone_app')
def phone_app():
    return render_template('phone_app.html')

@app.route('/dashboard')
@is_logged_in
def dashboard():
    return render_template('user.html')

@app.route('/user')
@is_logged_in
def user():
    return render_template('user.html')




@app.route('/login',methods=['GET','POST'])
def login():
	if request.method == 'POST':
		#get credentials
		username = request.form['username']
		password_candidate = request.form['password']

		#create cursor
		cur = mysql.connection.cursor()

		# get user by username
		result = cur.execute("SELECT * FROM UserDB WHERE Username = %s",[username])

		if result > 0:
			# get stored hash
			data = cur.fetchone() # get only first row
			password = data['Password']	
			name = data['Name']
            		email = data['Email']
			#compare passwords
			if sha256_crypt.verify(password_candidate,password):
			    #appe.logger.info('PASSWORD MATCHED')
			    session['logged_in'] = True
			    session['username'] = username
			    session['name'] = name
			    session['email'] = email

			    flash('You are now logged in','success')
			    return redirect(url_for('dashboard'))
			else:
			    #app.logger.info('PASSWORD NOT MATCHED')
			    error = 'Invalid Password'
			    return render_template('login.html',error=error)
		else:
			error = 'Username Not Found'
			return render_template('login.html',error=error)
	return render_template('login.html')

@app.route('/login_comp',methods=['GET','POST'])
def login_comp():
	if request.method == 'POST':
		#get credentials
		username = request.form['username']
		password_candidate = request.form['password']

		#create cursor
		cur = mysql.connection.cursor()

		# get user by username
		result = cur.execute("SELECT * FROM CompanyDB WHERE Username = %s",[username])

		if result > 0:
			# get stored hash
			data = cur.fetchone() # get only first row
			password = data['Password']	
			name = data['Name']
			#compare passwords
			if sha256_crypt.verify(password_candidate,password):
			    #appe.logger.info('PASSWORD MATCHED')
			    session['logged_in'] = True
			    session['username'] = username
			    session['name'] = name
			    flash('You are now logged in','success')
			    return redirect(url_for('dashboard'))		 		           
			else:
			    #app.logger.info('PASSWORD NOT MATCHED')
			    error = 'Invalid Password'
			    return render_template('login_comp.html',error=error)
		else:
			error = 'Username Not Found'
			return render_template('login_comp.html',error=error) 
	return render_template('login_comp.html')


@app.route('/logout')
def logout():
	session.clear()
	flash('You are now logged out','success')
	return redirect(url_for('login'))


'''@app.route('/mobile')
@is_logged_in2
def mobile():
    return render_template('mobileSurvey.html')

@app.route('/laptop')
def laptop():
    return render_template('laptopSurvey.html')

@app.route('/camera')
def camera():
    return render_template('cameraSurvey.html')

@app.route('/tv')
def tv():
    return render_template('tvSurvey.html')'''

@app.route('/admin')
def admin():
	return "Admin"


# USING WTFORMS MAKING A FORM CLASS WITH INBUILT VALIDATIONS
class Signup(Form):
    name = StringField('Name',[validators.Length(min = 1, max = 50)], render_kw={"placeholder": "Name"})
    email = StringField('Email',[validators.Length(min = 6, max = 50)], render_kw={"placeholder": "Email"})
    username = StringField('Username',[validators.Length(min = 4, max = 25)], render_kw={"placeholder": "Username"})
    password = PasswordField('Password',[
        validators.DataRequired(),
        validators.EqualTo('confirm',message = 'Passwords do not match')
        ], render_kw={"placeholder": "Password"})
    confirm = PasswordField('Confirm Password', render_kw={"placeholder": "Confirm Password"})

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
    name = StringField('Name',[validators.Length(min = 1, max = 50)], render_kw={"placeholder": "Name"})
    company_name = StringField('Company',[validators.Length(min = 1, max = 50)], render_kw={"placeholder": "Company Name"})
    website = StringField('Website',[validators.Length(min = 1, max = 50)], render_kw={"placeholder": "Website"})
    username = StringField('Username',[validators.Length(min = 4, max = 25)], render_kw={"placeholder": "Username"})
    email = StringField('Email',[validators.Length(min = 6, max = 50)], render_kw={"placeholder": "Email"})
    password = PasswordField('Password',[
        validators.DataRequired(),
        validators.EqualTo('confirm',message = 'Passwords do not match')
        ], render_kw={"placeholder": "Password"})
    confirm = PasswordField('Confirm Password', render_kw={"placeholder": "Confirm Password"})

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
