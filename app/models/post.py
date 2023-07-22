from db import db 


class Post(db.Model):
    id_post = db.Column(db.Integer, primary_key=True)
    title_post = db.Column(db.String, unique=False, nullable=False)
    content_post = db.Column(db.String, unique=False, nullable=False)
    creation_date_post = db.Column(db.DateTime, unique=False, nullable=False)
    modification_date_post = db.Column(db.DateTime, unique=False, nullable=True)
    view = db.Column(db.Integer, unique=False, nullable=False)
    id_user = db.Column(db.Integer, unique=False, nullable=False)