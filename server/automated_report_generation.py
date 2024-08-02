from flask import Blueprint, render_template

automated_report = Blueprint("automated_report", __name__)


@automated_report.route("/report_view")
def building_crm_view():
    return render_template("/automated_report_generation/automated_report_view.html")
