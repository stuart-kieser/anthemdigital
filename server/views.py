from flask import Blueprint, render_template, request, url_for, redirect, flash
from .models import Contact
from .database import db

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("home.html")


@views.route("/contact", methods=["POST"])
def contact():
    name = request.form["name"]
    email = request.form["email"]
    company = request.form["company"]
    message = request.form["message"]
    contact = Contact(name=name, email=email, company=company, message=message)
    print(name, email, company, message)
    db.session.add(contact)
    db.session.commit()
    return redirect(url_for("views.home"))
