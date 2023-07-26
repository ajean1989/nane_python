from db import db 


class Comment(db.Model):
    id_com = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer, unique=False, nullable=False)
    content_com = db.Column(db.Text, unique=False, nullable=False)
    creation_date_comment = db.Column(db.DateTime, unique=False, nullable=False)
    modification_date_comment = db.Column(db.DateTime, unique=False, nullable=True)
    id_user = db.Column(db.Integer, unique=False, nullable=False)
    id_recipe = db.Column(db.Integer, unique=False, nullable=True)
    id_post = db.Column(db.Integer, unique=False, nullable=True)

    def create_comment(username, password, email, birth, gender, regime):
        pass

    def get_comment(user_id=False, username=False, email=False):
        pass

    def modify_comment():
        pass

    def delete_comment():
        pass