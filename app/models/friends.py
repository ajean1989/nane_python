from db import db 


class Friends(db.Model):
    user_id = db.Column(db.Integer, unique=False, nullable=True)
    users_id = db.Column(db.JSON, unique=False, nullable=True)
