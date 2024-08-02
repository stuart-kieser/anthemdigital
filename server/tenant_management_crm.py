from flask import Blueprint, render_template, request, redirect, url_for
from .models import ContactForm
from .database import db

tenant_crm = Blueprint("tenant_crm", __name__)


@tenant_crm.route("/crm_view")
def tenant_crm_view():
    return render_template("/tenant_management_crm/tenant_crm_view.html")
