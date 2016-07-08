# -*- coding:utf-8 -*-
from app import create_app, db
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manage

app = create_app()
manager = Manager(app)


if  __name__ == '__main__':
    manager.run()