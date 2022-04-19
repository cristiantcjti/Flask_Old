from flask import Flask
from flask_migrate import Migrate
from .model import configure as config_db
from .serializer import configure as config_ma 

def create_app(): 
    # Config. app
    app = Flask(__name__)
    
    # Config. SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/library.db'
    # Block message of deprecated
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Config. database
    config_db(app)

    # Config. serealizer
    config_ma(app)

    # Config. migration 
    Migrate(app, app.db)

    from .books import bp_books
    app.register_blueprint(bp_books)


    return app

