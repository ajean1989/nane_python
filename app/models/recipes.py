from db import db 


class Recipes(db.Model):
    recipe_id = db.Column(db.Integer, primary_key=True)
    image_id = db.Column(db.Integer, unique=True, nullable=True)
    intro = db.Column(db.String, unique=False, nullable=False)
    name = db.Column(db.String, unique=False, nullable=False)
    type = db.Column(db.Integer, unique=False, nullable=False)
    quantity = db.Column(db.Integer, unique=False, nullable=False)
    video = db.Column(db.String, unique=False, nullable=True)
    date = db.Column(db.TIMESTAMP, unique=False, nullable=False)
    modification_date = db.Column(db.DateTime, unique=False, nullable=True)
    status = db.Column(db.Integer, unique=False, nullable=False)
    regime = db.Column(db.Integer, unique=False, nullable=False)
