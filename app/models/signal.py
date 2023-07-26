from db import db 

Signal_table = db.Table(
    "signal",
    db.Column('id_user_signaling', db.Integer,db.ForeignKey('user.id_user'), unique=False, nullable=False),
    db.Column('id_user_signaled', db.Integer, db.ForeignKey('user.id_user'), unique=False, nullable=False),
    db.Column('id_recipe', db.Integer, db.ForeignKey('recipe.id_recipe'), unique=False, nullable=True),
    db.Column('id_post', db.Integer, db.ForeignKey('post.id_post'), unique=False, nullable=True),
    db.Column('id_com', db.Integer, db.ForeignKey('comment.id_com'), unique=False, nullable=True),
    db.Column('id_img', db.Integer, db.ForeignKey('img.id_img'), unique=False, nullable=True),

    db.Column('creation_date_signal', db.DateTime, unique=False, nullable=False),
    db.Column('content_signal', db.Text, unique=False, nullable=True)
)
