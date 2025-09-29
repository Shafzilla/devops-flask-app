from flask import Flask

app = Flask(__name__)

@app.route('/')
def say_hello():
	return '<a href="http://localhost:5000/about">about page</a><br><a href="http://localhost:5000/contact"><Contact page</a>'

@app.route('/about')
def about():
	return '<p>This application is running on the Flask web framework. To learn more about this, go to</p><a href="https://flask.palletsprojects.com/en/stable/">Flask</a>'

def contact():
	return '<p>C23502209@mytudublin.ie</p>'

def form():
	return '<p>fill the form</p>'
