from flask import Blueprint, render_template

building_crm = Blueprint("building_crm", __name__)


@building_crm.route("/crm_view")
def building_crm_view():
    return render_template("/building_management_crm/building_crm_view.html")
