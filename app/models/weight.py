from db import db 


class weight(db.Model):
    recipe_id = db.Column(db.Integer, unique=False, nullable=False)
    ingredient_id = db.Column(db.Integer, unique=False, nullable=False)
    weight = db.Column(db.Integer, unique=False, nullable=False)
