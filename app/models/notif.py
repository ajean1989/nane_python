from db import db 


class Notif(db.Model):
    id_notify = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer, unique=False, nullable=False)
    response = db.Column(db.Integer, unique=False, nullable=True)
    creation_date_notif = db.Column(db.DateTime, unique=False, nullable=False)
    id_user = db.Column(db.Integer, unique=False, nullable=False)
    id_recipe = db.Column(db.Integer, unique=False, nullable=True)
    id_post = db.Column(db.Integer, unique=False, nullable=True)
    id_like = db.Column(db.Integer, unique=False, nullable=True)
