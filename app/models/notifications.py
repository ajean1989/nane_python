from db import db 


class Notifications(db.Model):
    notification_id  = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=False, nullable=False)
    recipe_id = db.Column(db.Integer, unique=False, nullable=True)
    like_id = db.Column(db.Integer, unique=False, nullable=True)
    com_id = db.Column(db.Integer, unique=False, nullable=True)
    type = db.Column(db.Integer, unique=False, nullable=False)
    status = db.Column(db.Integer, unique=False, nullable=False)
