from flask import Flask
import redis, json
import time

cache_expiry = 600

def expired_cache(cached_time):
    return time.time() - cached_time > cache_expiry

r = redis.Redis(host='redis-server', port=6379,
                decode_responses=True)

app = Flask(__name__)

@app.route('/')
def say_hello():
    data = r.get('hello')
    if data is not None:
        data = json.loads(data)
    if expired_cache(data['time']):
        return data['html']
    data =  '<a href="http://localhost:5000/about">about page</a><br><a href="http://localhost:5000/contact"><Contact page</a>'
    r.set('about', json.dumps({
        'html': data,
        'time': time.time()
    }))
    return data

@app.route('/about')
def about():
    data = r.get('about')
    if data is not None:
        data = json.loads(data)
    if expired_cache(data['time']):
        return data['html']
    data = '<p>This application is running on the Flask web framework. To learn more about this, go to</p><a href="https://flask.palletsprojects.com/en/stable/">Flask</a>' # Put your old HTML f-string here!
    r.set('about', json.dumps({
        'html': data,
        'time': time.time()
    }))
    return data
@app.route('/contact')
def contact():
    data = r.get('contact')
    if data is not None:
        data = json.loads(data)
    if expired_cache(data['time']):
        return data['html']
    data = '<p>c23502209@mytudublin.ie</p>'
    r.set('about', json.dumps({
        'html': data,
        'time': time.time()
    }))
    return data


@app.route('/form')
def form():
    data = r.get('form')
    if data is not None:
        data = json.loads(data)
    if expired_cache(data['time']):
        return data['html']
    data = '<p>fill the form</p>'
    r.set('about', json.dumps({
        'html': data,
        'time': time.time()
    }))
    return data


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
