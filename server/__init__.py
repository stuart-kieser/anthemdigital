from flask import Flask
from .views import views
from .database import db
from dotenv import load_dotenv

app = Flask(__name__)


def create_app():

    app.config["SECRET_KEY"] = load_dotenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
    db.init_app(app)

    app.register_blueprint(views, url_prefix="/")

    with app.app_context():
        # remember to:
        db.create_all()
        # add_data()
        db.session.commit()

    return app
