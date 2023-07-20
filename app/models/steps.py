from db import db 


class Steps(db.Model):
    recipe_id = db.Column(db.Integer, primary_key=True)
    image_id = db.Column(db.Integer, unique=False, nullable=True)
    number = db.Column(db.Integer, unique=False, nullable=False)
    description = db.Column(db.String, unique=False, nullable=False)
