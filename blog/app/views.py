# -*- coding:utf-8 -*-

from flask import render_template, flash, redirect
from .forms import LoginForm
from app import app
from flask.ext.login import login_required

# 首页
@app.route('/', methods = ['GET', 'POST']) 
@app.route('/index')
def index():
    return render_template('index.html', title = 'Home')

# 帖子页
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

# 登陆
@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for Name: ' + form.name.data)
        flash('passwd: ' + str(form.password.data))
        flash('remember_me ' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title = 'Sign In', form = form)