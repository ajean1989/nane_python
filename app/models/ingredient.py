from db import db 


class Ingredient(db.Model):
    id_ingredient = db.Column(db.Integer, primary_key=True)
    name_ingredient = db.Column(db.String(32), unique=True, nullable=False)
