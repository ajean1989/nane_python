from db import db 


class Posts(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=False, nullable=False)
    content = db.Column(db.String, unique=False, nullable=True)
    image_id = db.Column(db.Integer, unique=False, nullable=True)