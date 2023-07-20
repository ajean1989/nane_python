from db import db 


class Coms(db.Model):
    com_id = db.Column(db.Integer, unique=True, nullable=False)
    content = db.Column(db.String, unique=False, nullable=False)
    response_com_id = db.Column(db.Integer, unique=False, nullable=True)
    recipe_id = db.Column(db.Integer, unique=False, nullable=False)
    post_id = db.Column(db.Integer, unique=False, nullable=True)
