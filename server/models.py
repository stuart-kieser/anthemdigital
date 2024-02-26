from .database import db


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    company = db.Column(db.String(50))
    message = db.Column(db.String(200))
