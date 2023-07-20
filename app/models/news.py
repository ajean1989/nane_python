from db import db 


class News(db.Model):
    user_id = db.Column(db.Integer, unique=False, nullable=False)
    recipes_id = db.Column(db.JSON, unique=False, nullable=False)
    posts_id = db.Column(db.JSON, unique=False, nullable=False)
