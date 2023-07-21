from db import db 


class Friends(db.Model):
    id_friend = db.Column(db.Integer, unique=True, nullable=False)
    id_user = db.Column(db.Integer, unique=True, nullable=False)
    list_friends = db.Column(db.JSON, unique=False, nullable=True)
