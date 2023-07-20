from db import db 


class Myweek(db.Model):
    user_id = db.Column(db.Integer, unique=True, nullable=True)
    schedule = db.Column(db.JSON, unique=False, nullable=True)
