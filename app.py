from flask import Flask

app = Flask(__name__) # object called app is created of Flask class

@app.route('/')
def index():
	return '<html><body><h1>This is My Python Web App </h1></body></html>'

if __name__ == '__main__':
	app.run(debug = True)
