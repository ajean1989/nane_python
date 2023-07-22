from db import db 


class Friend(db.Model):
    id_friend = db.Column(db.Integer, primary_key=True)
    list_friends = db.Column(db.JSON, unique=False, nullable=True)
    id_user = db.Column(db.Integer, unique=True, nullable=False)
