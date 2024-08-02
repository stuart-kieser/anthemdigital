from flask import Flask
from .views import views
from .tenant_management_crm import tenant_crm
from .building_management_crm import building_crm
from .maintenance_management_dash import maintenance_crm
from .automated_report_generation import automated_report
from .database import db
from dotenv import load_dotenv

app = Flask(__name__)


def create_app():

    app.config["SECRET_KEY"] = load_dotenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
    db.init_app(app)

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(tenant_crm, url_prefix="/tcrm")
    app.register_blueprint(building_crm, url_prefix="/bcrm")
    app.register_blueprint(maintenance_crm, url_prefix="/mcrm")
    app.register_blueprint(automated_report, url_prefix="/automated_report")

    with app.app_context():
        # remember to:
        db.create_all()
        # add_data()
        db.session.commit()

    return app
