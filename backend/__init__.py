from flask import Flask, Blueprint
from flask_cors import CORS

from .src.db import db, Config
from .src.routes import main

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config["DEBUG"] = True
    #DB set config
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
    app.config["SQLALCHEMY_DATABASE_URI"] = Config.SQLALCHEMY_DATABASE_URI
    #DB init
    db.init_app(app)
    with app.app_context():
        db.create_all()
        db.session.commit()
    app.register_blueprint(main)

    return app
