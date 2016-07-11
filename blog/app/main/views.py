from flask import render_template, redirect, url_for, session
from datetime import datetime
from . import main
from app.forms import PostForm
from flask_login import current_user
from ..models import Post
from .. import db


@main.route('/', methods = ['GET', 'POST'])
def index():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body = form.body.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('.index'))
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('index.html', current_time = datetime.utcnow(), form = form, posts = posts)

@main.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404