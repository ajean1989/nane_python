from db import db 


class Recipe_ingredient_int(db.Model):
    id_recipe = db.Column(db.Integer, unique=False, nullable=False)
    id_ingredient = db.Column(db.Integer, unique=False, nullable=False)
    weight = db.Column(db.Integer, unique=False, nullable=False)
