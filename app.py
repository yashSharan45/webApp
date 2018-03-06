import os

from exceptions import Exception
from flask import Flask, render_template, flash, request, redirect, url_for, session, logging, request, send_from_directory, jsonify
from pip._vendor.requests.compat import str
from wtforms import Form, StringField , TextAreaField, PasswordField, validators
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt
from functools import wraps
from flask_mail import Mail, Message
from werkzeug import secure_filename
from werkzeug.exceptions import BadRequest


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



# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'uploads/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 
'jpeg', 'gif'])
# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and  filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']
# This route will show a form to perform an AJAX request jQuery is 
# loaded to execute the request and update the value of the operation



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

@app.route('/',methods=['GET','POST'])
def index():    
    if request.method == 'POST':
        fname = request.form['firstname']
        lname = request.form['lastname']
        email = request.form['email']
        country = request.form['country']
        subject = request.form['subject']
        info = "Contact Us Form Details" + '\n\n' + fname + ' ' + lname + '\n' + email + '\n' + country + '\n' + subject
        send_mail(info)
    
    return render_template('index.html')

@app.route('/index',methods=['GET','POST'])
def index1():
    if request.method == 'POST':
        fname = request.form['firstname']
        lname = request.form['lastname']
        email = request.form['email']
        country = request.form['country']
        subject = request.form['subject']
        info = "Contact Us Form Details" + '\n\n' + fname + ' ' + lname + '\n' + email + '\n' + country + '\n' + subject
        send_mail(info)
    return render_template('index.html')

def send_mail(suggestions):
    #app.logger.info('%s',suggestions)
    if suggestions != "":
    	msg = Message('FEEDBACK', sender = 'aneeshverma0412@gmail.com', recipients = ['aneeshverma0412@gmail.com'])
    	msg.body = suggestions
    	mail.send(msg)

# ROUTING OF PHONES
@app.route('/phones')
def phones():
    return render_template('phones.html')

@app.route('/phones/iphoneX',methods=['GET','POST'])
def phone1():
    if request.method == 'POST':
        #sending mail from data acquired from textbox
        suggestions = request.form['text']
        send_mail(suggestions)
        # get data through invisible form
        email = request.form['email']
        category = request.form['category']
        product = request.form['product']
        rating = request.form['starwar']


        #Create Cursor
        cur = mysql.connection.cursor()

        # if same survey already submitted
        result = cur.execute("SELECT * FROM SurveyDB WHERE Email = %s and Categories = %s and Products = %s",[email,category,product])
        if result > 0:
            flash('You can submit the forms only once','danger')
            return redirect(url_for('user'))
        try:
            app.logger.info('%s %s %s %s ',email,category,product,rating)
            cur.execute("INSERT INTO SurveyDB(Email,Categories,Products,Rating) VALUES (%s,%s,%s,%s)",(email,category,product,rating))
            mysql.connection.commit()
            cur.close()
            flash('Survey submitted successfully','success')
            return redirect(url_for('user'))
        except Exception as e:
            exception_user = e
                
    return render_template('phones/iphoneX.html')

@app.route('/phones/pixel2',methods=['GET','POST'])
def phone2():
    if request.method == 'POST':
        #sending mail from data acquired from textbox
        suggestions = request.form['text']
        send_mail(suggestions)
        # get data through invisible form
        email = request.form['email']
        category = request.form['category']
        product = request.form['product']
        rating = request.form['starwar']


        #Create Cursor
        cur = mysql.connection.cursor()

        # if same survey already submitted
        result = cur.execute("SELECT * FROM SurveyDB WHERE Email = %s and Categories = %s and Products = %s",[email,category,product])
        if result > 0:
            flash('You can submit the forms only once','danger')
            return redirect(url_for('user'))
        try:
            app.logger.info('%s %s %s %s ',email,category,product,rating)
            cur.execute("INSERT INTO SurveyDB(Email,Categories,Products,Rating) VALUES (%s,%s,%s,%s)",(email,category,product,rating))
            mysql.connection.commit()
            cur.close()
            flash('Survey submitted successfully','success')
            return redirect(url_for('user'))
        except Exception as e:
            exception_user = e
                
    return render_template('phones/pixel2.html')

@app.route('/phones/SamsungS8',methods=['GET','POST'])
def phone3():
    if request.method == 'POST':
        #sending mail from data acquired from textbox
        suggestions = request.form['text']
        send_mail(suggestions)
        # get data through invisible form
        email = request.form['email']
        category = request.form['category']
        product = request.form['product']
        rating = request.form['starwar']


        #Create Cursor
        cur = mysql.connection.cursor()

        # if same survey already submitted
        result = cur.execute("SELECT * FROM SurveyDB WHERE Email = %s and Categories = %s and Products = %s",[email,category,product])
        if result > 0:
            flash('You can submit the forms only once','danger')
            return redirect(url_for('user'))
        try:
            app.logger.info('%s %s %s %s ',email,category,product,rating)
            cur.execute("INSERT INTO SurveyDB(Email,Categories,Products,Rating) VALUES (%s,%s,%s,%s)",(email,category,product,rating))
            mysql.connection.commit()
            cur.close()
            flash('Survey submitted successfully','success')
            return redirect(url_for('user'))
        except Exception as e:
            exception_user = e
                
    return render_template('phones/SamsungS8.html')

@app.route('/phones/oneplus5T',methods=['GET','POST'])
def phone4():
    if request.method == 'POST':
        #sending mail from data acquired from textbox
        suggestions = request.form['text']
        send_mail(suggestions)
        # get data through invisible form
        email = request.form['email']
        category = request.form['category']
        product = request.form['product']
        rating = request.form['starwar']


        #Create Cursor
        cur = mysql.connection.cursor()

        # if same survey already submitted
        result = cur.execute("SELECT * FROM SurveyDB WHERE Email = %s and Categories = %s and Products = %s",[email,category,product])
        if result > 0:
            flash('You can submit the forms only once','danger')
            return redirect(url_for('user'))
        try:
            app.logger.info('%s %s %s %s ',email,category,product,rating)
            cur.execute("INSERT INTO SurveyDB(Email,Categories,Products,Rating) VALUES (%s,%s,%s,%s)",(email,category,product,rating))
            mysql.connection.commit()
            cur.close()
            flash('Survey submitted successfully','success')
            return redirect(url_for('user'))
        except Exception as e:
            exception_user = e
                
    return render_template('phones/oneplus5T.html')
    
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
        email = request.form['email']
        category = request.form['category']
        product = request.form['product']
        rating = request.form['starwar']


        #Create Cursor
        cur = mysql.connection.cursor()

        # if same survey already submitted
        result = cur.execute("SELECT * FROM SurveyDB WHERE Email = %s and Categories = %s and Products = %s",[email,category,product])
        if result > 0:
        	flash('You can submit the forms only once','danger')
		return redirect(url_for('user'))
        try:
        	cur.execute("INSERT INTO SurveyDB(Email,Categories,Products,Rating) VALUES (%s,%s,%s,%s)",(email,category,product,rating))
        	mysql.connection.commit()
        	cur.close()
        	flash('Survey submitted successfully','success')
        	return redirect(url_for('user'))
        except Exception as e:
        	exception_user = e
        
        #app.logger.info('%s %s %s %s ',email,category,product,rating)
        
    return render_template('laptops/mac.html')

@app.route('/laptops/alienware',methods=['GET','POST'])
def lappy2():
    if request.method == 'POST':
        #sending mail from data acquired from textbox
        suggestions = request.form['text']
        send_mail(suggestions)
        # get data through invisible form
        email = request.form['email']
        category = request.form['category']
        product = request.form['product']
        rating = request.form['starwar']


        #Create Cursor
        cur = mysql.connection.cursor()

        # if same survey already submitted
        result = cur.execute("SELECT * FROM SurveyDB WHERE Email = %s and Categories = %s and Products = %s",[email,category,product])
        if result > 0:
            flash('You can submit the forms only once','danger')
            return redirect(url_for('user'))
        try:
            app.logger.info('%s %s %s %s ',email,category,product,rating)
            cur.execute("INSERT INTO SurveyDB(Email,Categories,Products,Rating) VALUES (%s,%s,%s,%s)",(email,category,product,rating))
            mysql.connection.commit()
            cur.close()
            flash('Survey submitted successfully','success')
            return redirect(url_for('user'))
        except Exception as e:
            exception_user = e
        
        #app.logger.info('%s %s %s %s ',email,category,product,rating)
        
    return render_template('laptops/alienware.html')

@app.route('/laptops/yoga',methods=['GET','POST'])
def lappy3():
    if request.method == 'POST':
        #sending mail from data acquired from textbox
        suggestions = request.form['text']
        send_mail(suggestions)
        # get data through invisible form
        email = request.form['email']
        category = request.form['category']
        product = request.form['product']
        rating = request.form['starwar']


        #Create Cursor
        cur = mysql.connection.cursor()

        # if same survey already submitted
        result = cur.execute("SELECT * FROM SurveyDB WHERE Email = %s and Categories = %s and Products = %s",[email,category,product])
        if result > 0:
            flash('You can submit the forms only once','danger')
            return redirect(url_for('user'))
        try:
            app.logger.info('%s %s %s %s ',email,category,product,rating)
            cur.execute("INSERT INTO SurveyDB(Email,Categories,Products,Rating) VALUES (%s,%s,%s,%s)",(email,category,product,rating))
            mysql.connection.commit()
            cur.close()
            flash('Survey submitted successfully','success')
            return redirect(url_for('user'))
        except Exception as e:
            exception_user = e
        
        #app.logger.info('%s %s %s %s ',email,category,product,rating)
        
    return render_template('laptops/yoga.html')

@app.route('/laptops/spectre',methods=['GET','POST'])
def lappy4():
    if request.method == 'POST':
        #sending mail from data acquired from textbox
        suggestions = request.form['text']
        send_mail(suggestions)
        # get data through invisible form
        email = request.form['email']
        category = request.form['category']
        product = request.form['product']
        rating = request.form['starwar']


        #Create Cursor
        cur = mysql.connection.cursor()

        # if same survey already submitted
        result = cur.execute("SELECT * FROM SurveyDB WHERE Email = %s and Categories = %s and Products = %s",[email,category,product])
        if result > 0:
            flash('You can submit the forms only once','danger')
            return redirect(url_for('user'))
        try:
            app.logger.info('%s %s %s %s ',email,category,product,rating)
            cur.execute("INSERT INTO SurveyDB(Email,Categories,Products,Rating) VALUES (%s,%s,%s,%s)",(email,category,product,rating))
            mysql.connection.commit()
            cur.close()
            flash('Survey submitted successfully','success')
            return redirect(url_for('user'))
        except Exception as e:
            exception_user = e
                
    return render_template('laptops/spectre.html')


# ROUTING OF GADGETS
@app.route('/gadgets',methods=['GET','POST'])
def gadgets():
    if request.method == 'POST': # if get then not redirecting
        email = request.values.get('eemail')
        flash('You are subscribed with us :)','info')
        email = 'SUBSCRIBE THIS PERSON : ' + email
        app.logger.info("%s",email)
        send_mail(email)
        return redirect(url_for('user'))
    return render_template('gadgets.html')


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

@app.route('/mobile_suggestions',methods=['GET','POST'])
@is_logged_in
def mob_sug():
    ram = request.args.get('radio1') # GET REQUEST
    rom = request.args.get('radio2')
    screen = request.args.get('radio3')
    if screen == '5-5.5':
        str.split("-")
        app.logger.info("SS" +"str")
    rear_cam = request.args.get('radio4')
    front_cam = request.args.get('radio5')
    price = request.args.get('radio6')
    #app.logger.info("%s %s %s %s %s %s ",ram,rom,screen,rear_cam,front_cam,price)
    
    #Create Cursor
    cur = mysql.connection.cursor()
    # get user by email
    result = cur.execute("SELECT * FROM MobileDB WHERE Ram = %s",[ram]) 
    #app.logger.info("%s",screen)   
    #result = cur.execute("SELECT * FROM MobileDB WHERE Screen_size = %s",[screen])    
    if result > 0:
        mysql.connection.commit()

        #data = cur.fetchone() # get only first row
        data = cur.fetchall()
        for row in data:
            app.logger.info("%s",row)    
        # Setting session data
        #session['name_mobile'] = data['Name']
        #app.logger.info("%s",session['name_mobile'])
    cur.close()
    return render_template('mobile_suggestions.html')

@app.route('/laptop_suggestions')
@is_logged_in
def lap_sug():
    return render_template('laptop_suggestions.html')

@app.route('/user',methods = ['GET','POST'])
@is_logged_in
def user():
    ####################### Profile Pic ########################################
    #Create Cursor
    cur = mysql.connection.cursor()
    # get user by email
    result = cur.execute("SELECT * FROM RatingDB WHERE email = %s",[session['email']])    
    if result > 0:
        mysql.connection.commit()

        data = cur.fetchone() # get only first row
        # Setting session data
        session['img'] = data['imgSrc']
        #app.logger.info("%s",session['img'])
    cur.close()
    ####################### ON LOAD OF USER PROFILE ############################
    #Create Cursor
    cur = mysql.connection.cursor()
    # get user by email
    result = cur.execute("SELECT * FROM User_infoDB WHERE email = %s",[session['email']])    
    if result > 0:
        #app.logger.info('%s',result)
        mysql.connection.commit()

        data = cur.fetchone() # get only first row
        # Setting session data
        session['phone'] = data['Phone']
        session['gender'] = data['Gender']
        session['address'] = data['Address']
        session['city'] = data['City']
        session['country'] = data['Country']
        session['postal'] = data['Postal']
        session['about'] = data['About']
        #app.logger.info('%s',data['About'])

    ########################### ON SUBMIT #######################################
    if request.method == 'POST':
        """
        if request.form['submit'] == 'Main':
            #return render_template('gadgets.html')
            return redirect(url_for('gadgets'))
        elif request.form['submit2'] == 'Main2':
            return redirect(url_for('laptops'))

            ### VERY IMPORTANT .. IF WANT TO ACCESS TWO FORMS IN SAME HTML PAGE THEN 
                GIVE DIFFERENT NAME AND VALUES TO THE SUBMIT BUTTONS OF THOSE FORMS
                AND ACCESS THEM WITH " request.form['buttonName'] == 'buttonValue' "            
        """    
        phone = request.form['phone']
        gender = request.form['gender']
        address = request.form['home']
        city = request.form['city']
        country = request.form['country']
        postal = request.form['postal']
        about = request.form['about']
        email = request.form['email']
        #app.logger.info("%s %s %s %s %s %s %s %s",phone,gender,address,city,country,postal,email,about)
        
        # get user by email
        result = cur.execute("SELECT * FROM User_infoDB WHERE email = %s",[email])
        flag = False
        if result <= 0:
            cur.execute("INSERT INTO User_infoDB(Email) VALUES (%s)",[email])
        
        if phone != "":
            flag = True
            cur.execute("UPDATE User_infoDB SET Phone = %s WHERE Email = %s",(phone,email));
        
        if gender != "":
            flag = True
            cur.execute("UPDATE User_infoDB SET Gender = %s WHERE Email = %s",(gender,email));
        
        if address != "":
            flag = True
            cur.execute("UPDATE User_infoDB SET address = %s WHERE Email = %s",(address,email));

        if city != "":
            flag = True
            cur.execute("UPDATE User_infoDB SET city = %s WHERE Email = %s",(city,email));
        
        if country != "":
            flag = True
            cur.execute("UPDATE User_infoDB SET country = %s WHERE Email = %s",(country,email));

        if postal != "":
            flag = True
            cur.execute("UPDATE User_infoDB SET postal = %s WHERE Email = %s",(postal,email));
        
        if about != "":
            flag = True
            cur.execute("UPDATE User_infoDB SET about = %s WHERE Email = %s",(about,email));

        mysql.connection.commit()
        if flag == True:    
            flash('Changes will be visible the next time you visit User Profile','info')
    cur.close()
    
    return render_template('user.html')

"""
cursor.execute ("
   UPDATE tblTableName
   SET Year=%s, Month=%s, Day=%s, Hour=%s, Minute=%s
   WHERE Server=%s
", (Year, Month, Day, Hour, Minute, ServerID))
"""

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
			    return redirect(url_for('user'))
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

#change password
@app.route('/password_update',methods=['GET','POST'])
def password_update():
    if request.method == 'POST':
        email = request.form['form-email']
        old_password = request.form['form-password']
        new_password = request.form['new-password']
        
        #Create Cursor
        cur = mysql.connection.cursor()

        #Check if Email already exists
        result = cur.execute("SELECT * FROM UserDB where Email = %s",[email])
        if result > 0:
            app.logger.info('%s',result)
            data = cur.fetchone() # get only first row
            password = data['Password']
            if sha256_crypt.verify(old_password,password):
                new_password = sha256_crypt.encrypt(str(new_password))
                cur.execute("UPDATE UserDB SET Password = %s WHERE Email = %s",(new_password,email));
                app.logger.info('%s %s',old_password,new_password)
            else:
                flash('Incorrect Password','danger')
                return render_template('changepass.html')

        #Commit to DB
        mysql.connection.commit()

        #Close Connection
        cur.close()             
        flash('Password Updated','success')
        return redirect(url_for('user'))
    return render_template('changepass.html')

@app.route('/upload', methods=['POST']) 
def upload():

    try:
        # Get the name of the uploaded file
        file = request.files['file']
        # Check if the file is one of the allowed types/extensions
        if file and allowed_file(file.filename):
            # Make the filename safe, remove unsupported chars
            filename = secure_filename(file.filename)
            # Move the file form the temporal folder to the upload folder we 
            # setup
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # Redirect the user to the uploaded_file route, which will 
            # basicaly show on the browser the uploaded file
            #return redirect(url_for('uploaded_file',filename=filename))
            #app.logger.info('%s',filename)
            
            #Create Cursor
            cur = mysql.connection.cursor()

            # get user by email
            result = cur.execute("SELECT * FROM RatingDB WHERE email = %s",[session['email']])
            if result <= 0:
                cur.execute("INSERT INTO RatingDB(Email) VALUES (%s)",[session['email']])
            cur.execute("UPDATE RatingDB SET imgSrc = %s WHERE Email = %s",(file.filename,[session['email']]));
            mysql.connection.commit()
            cur.close()    
        else:
            flash("Error uploading file",'danger')    
        return redirect(url_for('user'))
    except Exception as e:
        flash("Please Select a photo ",'danger')
        return redirect(url_for('user'))
        #raise BadRequest('Something Went Wrong!!')
    
# This route is expecting a parameter containing the name of a file. 
# Then it will locate that file on the upload directory and show it on 
# the browser, so if the user uploads an image, that image is going to 
# be show after the upload
@app.route('/uploads/<filename>') 
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


if __name__ == '__main__':
    app.secret_key = 'secretZone'
    app.run(debug = True)
