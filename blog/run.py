# -*- coding:utf-8 -*-
import os
from app import create_app, db
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Shell

app = create_app()
manager = Manager(app)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

def make_shell_context():
    return dict(app = app, db = db)
manager.add_command('shell', Shell(make_context = make_shell_context))

if  __name__ == '__main__':
    manager.run()