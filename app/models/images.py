from db import db 


class Images(db.Model):
    image_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Float, unique=False, nullable=False)
    type = db.Column(db.Integer, unique=False, nullable=False)
