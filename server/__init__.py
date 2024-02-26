from flask import Flask
from dotenv import load_dotenv
import os
from .database import db


# Create app function, Register SQL database
def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "this_secret_key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    db.init_app(app)

    from .views import views

    app.register_blueprint(views, url_prefix="/")

    with app.app_context():
        db.create_all()

    return app
