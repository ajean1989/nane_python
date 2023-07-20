from db import db 


class Log(db.Model):
    user_id = db.Column(db.Integer, unique=False, nullable=False)
    date = db.Column(db.DateTime, unique=False, nullable=False)
    seen_user_id = db.Column(db.Integer, unique=False, nullable=True)
    seen_recipe_id = db.Column(db.Integer, unique=False, nullable=True)
    seen_post_id = db.Column(db.Integer, unique=False, nullable=True)
