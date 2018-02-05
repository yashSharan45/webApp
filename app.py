from flask import Flask, render_template

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

@app.route('/signup')
def signup():
	return render_template('signup.html')

if __name__ == '__main__':
	app.run(debug = True)
