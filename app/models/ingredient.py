from db import db 


class Ingredient(db.Model):
    ingredient_id = db.Column(db.Integer, primary_key=True)
    name_ingredient = db.Column(db.String, unique=True, nullable=False)
