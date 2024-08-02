from flask import render_template, Blueprint

maintenance_crm = Blueprint("maintenance_crm", __name__)


@maintenance_crm.route("maintenance_crm")
def mainteannce_crm_view():
    return render_template(
        "/maintenance_management_dash/maintenance_management_dash.html"
    )
