from db import db 


class Img(db.Model):
    id_img = db.Column(db.Integer, primary_key=True)
    title_img = db.Column(db.String, unique=False, nullable=False)
    caption_img = db.Column(db.String, unique=False, nullable=True)
    link_img = db.Column(db.String, unique=True, nullable=False)
    id_user = db.Column(db.Integer, unique=False, nullable=True)
    id_recipe = db.Column(db.Integer, unique=False, nullable=True)
    id_post = db.Column(db.Integer, unique=False, nullable=True)
