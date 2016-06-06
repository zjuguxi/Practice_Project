# -*- coding:utf-8 -*-
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'} # 用户名
    return render_template('index.html', title = 'Home', user = user)