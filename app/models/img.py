from db import db 


class Img(db.Model):
    id_img = db.Column(db.Integer, primary_key=True)
    title_img = db.Column(db.String(32), unique=False, nullable=False)
    caption_img = db.Column(db.String(256), unique=False, nullable=True)
    link_img = db.Column(db.String(512), unique=True, nullable=False)
    id_user = db.Column(db.Integer, unique=False, nullable=True)
    id_recipe = db.Column(db.Integer, unique=False, nullable=True)
    id_post = db.Column(db.Integer, unique=False, nullable=True)

    def create_img():
        pass

    def get_img():
        pass

    def modify_img():
        pass

    def delete_img():
        pass