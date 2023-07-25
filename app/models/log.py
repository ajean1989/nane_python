from db import db 

"""
class Log(db.Model):
    id_user_0 = db.Column(db.Integer, unique=False, nullable=False)
    id_user_1 = db.Column(db.Integer, unique=False, nullable=True)
    id_recipe = db.Column(db.Integer, unique=False, nullable=True)
    id_post = db.Column(db.Integer, unique=False, nullable=True)
    id_com = db.Column(db.Integer, unique=False, nullable=True)
    id_ingredient = db.Column(db.Integer, unique=False, nullable=True)
    id_notifiy = db.Column(db.Integer, unique=False, nullable=True)
    id_history = db.Column(db.Integer, unique=False, nullable=True)
    id_like = db.Column(db.Integer, unique=False, nullable=True)
    date = db.Column(db.DateTime, unique=False, nullable=False)
    crud = db.Column(db.Integer, unique=False, nullable=False)
"""

Log_table = db.Table(
    "log",
    db.Column('id_user_0', db.Integer, db.ForeignKey('user.id_user')),
    db.Column('id_user_1', db.Integer, db.ForeignKey('user.id_user')),
    db.Column('id_recipe', db.Integer, db.ForeignKey('recipe.id_recipe')),
    db.Column('id_post', db.Integer, db.ForeignKey('post.id_post')),
    db.Column('id_com', db.ForeignKey('comment.id_com')),
    db.Column('id_ingredient', db.ForeignKey('ingredient.id_ingredient')),
    db.Column('id_notifi', db.ForeignKey('notif.id_notif')),
    db.Column('id_history', db.ForeignKey('history.id_history')),
    db.Column('id_like', db.ForeignKey('like.id_like')),

    db.Column('date_log', db.DateTime, unique=False, nullable=False),
    db.Column('crud', db.Integer, unique=False, nullable=False),
)
