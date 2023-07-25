from db import db 


class History(db.Model):
    id_history = db.Column(db.Integer, primary_key=True)
    search = db.Column(db.String(256), unique=False, nullable=True)
    user_id = db.Column(db.Integer, unique=False, nullable=False)
