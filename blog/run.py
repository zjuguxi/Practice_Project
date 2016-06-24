from flask import Flask
from flask_script import Manager
from flask_moment import Moment


app = Flask(__name__)
manager = Manager(app)
moment = Moment(app)

from app import views
if __name__ == '__main__':
    manager.run()