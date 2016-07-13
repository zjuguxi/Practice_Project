from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from config import config


moment = Moment ()
bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config['default'])
    config['default'].init_app(app)
    moment.init_app(app)
    bootstrap.init_app(app)
    db = SQLAlchemy(app)
    app.secret_key = 'SECRET_KEY'
    db.init_app(app)


    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app