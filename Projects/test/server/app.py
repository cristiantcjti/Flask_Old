from flask import Flask
from blueprints.googly_eyes import googly_eyes_bp
from flask_cors import CORS


def create_app(config_filename=None):
    app = Flask(__name__)
    CORS(app)
    if config_filename:
        app.config.from_pyfile(config_filename)

    app.register_blueprint(googly_eyes_bp)

    return app

