from db import db 


class Views(db.Model):
    recipe_id = db.Column(db.Integer, unique=False, nullable=False)
    view = db.Column(db.Integer, unique=False, nullable=False)
