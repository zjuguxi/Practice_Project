from flask import Flask
from views import  my_view
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)
manager = Manager(app)
boostrap = Bootstrap(app)
moment = Moment(app)


if __name__ == '__main__':
    manager.run()