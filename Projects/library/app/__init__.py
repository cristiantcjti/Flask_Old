from flask import Flask
from flask_migrate import Migrate
from .model import configure as config_db
from .serealizer import configure as config_ma 

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/library.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    config_db(app)

    Migrate(app, app.db)
    return app

