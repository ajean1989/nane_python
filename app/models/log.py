from db import db 


class Log(db.Model):
    id_user_0 = db.Column(db.Integer, unique=False, nullable=False)
    id_user_1 = db.Column(db.Integer, unique=False, nullable=True)
    id_recipe = db.Column(db.Integer, unique=False, nullable=True)
    id_post = db.Column(db.Integer, unique=False, nullable=True)
    id_com = db.Column(db.Integer, unique=False, nullable=True)
    id_ingredient = db.Column(db.Integer, unique=False, nullable=True)
    id_notifiy = db.Column(db.Integer, unique=False, nullable=True)
    id_history = db.Column(db.Integer, unique=False, nullable=True)
    id_like = db.Column(db.Integer, unique=False, nullable=True)
    date = db.Column(db.DateTime, unique=False, nullable=False)
    crud = db.Column(db.Integer, unique=False, nullable=False)