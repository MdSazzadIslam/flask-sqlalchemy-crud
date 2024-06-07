from flask import Flask
from flask_cors import CORS
from config import DATABASE_CONNECTION_URI
from routes.productRoute import products
from utils.db import db


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    CORS(app)

    app.register_blueprint(products)

    return app
