from db import db 


class Ingredients(db.Model):
    ingredient_id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.String, unique=False, nullable=True)
    name = db.Column(db.String, unique=True, nullable=False)
