from flask import Flask
import redis
import time

r = redis.Redis(host='redis-server', port=6379,
                decode_responses=True)
r.set('hello', 123)
print(r.get('hello'))

app = Flask(__name__)

@app.route('/')
def say_hello():
    return '<a href="http://localhost:5000/about">about page</a><br><a href="http://localhost:5000/contact"><Contact page</a>'

@app.route('/about')
def about():
    data = r.get('about')
    if data is not None:
        if time.time() - data['time'] > 600:
            return data['html']
    data = '<p>This application is running on the Flask web framework. To learn more about this, go to</p><a href="https://flask.palletsprojects.com/en/stable/">Flask</a>'
    r.set('about', {
        'html' : data,
        'time' : time.time()
    })
    return data

@app.route('/contact')
def contact():
    data = r.get('contact')
    if data is not None:
        if time.time() - data['time'] > 600:
            return data['html']
    data = '<p>c23502209@mytudublin.ie</p>'
    r.set('contact', {
        'html' : data,
        'time' : time.time()
    })
    return data

@app.route('/form')
def form():
    data = r.get('form')
    if data is not None:
        if time.time() - data['time'] > 600:
            return data['html']
    data = '<p>fill the form</p>'
    r.set('form', {
        'html' : data,
        'time' : time.time()
    })
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
