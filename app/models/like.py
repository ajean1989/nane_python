from db import db 


class Like(db.Model):
    id_like = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, unique=False, nullable=False)
    id_recipe = db.Column(db.Integer, unique=False, nullable=True)
    id_post = db.Column(db.Integer, unique=False, nullable=True)
    id_com = db.Column(db.Integer, unique=False, nullable=True)

    def create_like():
        pass

    def get_like():
        pass

    def modify_like():
        pass

    def delete_like():
        pass