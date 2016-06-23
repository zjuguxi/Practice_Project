from flask import render_template, redirect, url_for
from datetime import datetime
from run import app

@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html', current_time = datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name = name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404