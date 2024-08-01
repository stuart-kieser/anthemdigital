from flask import Blueprint, render_template, request, redirect, url_for
from .models import ContactForm
from .database import db

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("home.html")


@views.route("/contact-form", methods=["POST"])
def contact_form():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    contact_form = ContactForm(name=name, email=email, message=message)

    db.session.add(contact_form)
    db.session.commit()

    return redirect(url_for("views.home"))


@views.route("/terms-of-service")
def tos():
    return render_template("terms-of-service.html")


@views.route("/privacy-policy")
def pp():
    return render_template("privacy-policy.html")


@views.route("/about")
def about():
    return render_template("about.html")


@views.route("/contact-us")
def contact():
    return render_template("contact.html")


@views.route("/services")
def services():
    return render_template("services.html")


@views.route("/testimonials")
def testomonials():
    return render_template("testomonials.html")
