from flask import Flask
from .views import views

app = Flask(__name__)


def create_app():
    app.register_blueprint(views, url_prefix="/")

    with app.app_context():
        app.run(debug=True)

    return app
