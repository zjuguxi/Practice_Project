from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_moment import Moment
from flask_bootstrap import Bootstrap


moment = Moment ()
bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    db.init_app(app)
    moment.init_app(app)
    bootstrap.init_app(app)
    app.secret_key = 'SECRET_KEY'

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app