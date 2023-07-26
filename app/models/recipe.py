from db import db 


class Recipe(db.Model):
    id_recipe = db.Column(db.Integer, primary_key=True)
    title_recipe = db.Column(db.String(128), unique=False, nullable=False)
    intro = db.Column(db.Text, unique=False, nullable=False)
    content = db.Column(db.Text, unique=False, nullable=False)
    type_recipe = db.Column(db.Integer, unique=False, nullable=False)
    diet = db.Column(db.Integer, unique=False, nullable=False)
    quantity = db.Column(db.Integer, unique=False, nullable=False)
    video = db.Column(db.String(512), unique=False, nullable=True)
    creation_date_recipe = db.Column(db.DateTime, unique=False, nullable=False)
    modification_date_recipe = db.Column(db.DateTime, unique=False, nullable=True)
    statut = db.Column(db.Integer, unique=False, nullable=False)
    view = db.Column(db.Integer, unique=False, nullable=False)
    id_user = db.Column(db.Integer, unique=False, nullable=False)

    def create_recipe():
        pass

    def get_recipe():
        pass

    def modify_recipe():
        pass

    def delete_recipe():
        pass
