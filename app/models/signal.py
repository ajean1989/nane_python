from db import db 


class Signal(db.Model):
    id_user_signaling = db.Column(db.Integer, unique=False, nullable=False)
    id_user_signaled = db.Column(db.Integer, unique=False, nullable=False)
    id_recipe = db.Column(db.Integer, unique=False, nullable=True)
    id_post = db.Column(db.Integer, unique=False, nullable=True)
    id_com = db.Column(db.Integer, unique=False, nullable=True)
    id_img = db.Column(db.Integer, unique=False, nullable=True)
    creation_date_signal = db.Column(db.DateTime, unique=False, nullable=False)
    content_signal = db.Column(db.String, unique=False, nullable=True)
