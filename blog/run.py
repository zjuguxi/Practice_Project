from flask import Flask
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)
manager = Manager(app)
boostrap = Bootstrap(app)
moment = Moment(app)

from . import  views


if __name__ == '__main__':
    manager.run()