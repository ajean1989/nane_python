from db import db 
from flask import redirect, url_for
from sqlalchemy import text

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    image_id = db.Column(db.Integer, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, unique=False, nullable=False)
    birth = db.Column(db.DateTime, unique=False, nullable=False)
    gender = db.Column(db.String, unique=False, nullable=False)
    regime = db.Column(db.String, unique=False, nullable=False)
    status = db.Column(db.Integer, unique=False, nullable=False)


    def create_user(username, password, email, birth, gender, regime):
        #sql = f"INSERT INTO user (username, password, email, birth, gender, regime) VALUES ('{username}', '{password}', '{email}', '{birth}', '{genre}','{regime}')"
        sql = text("INSERT INTO user (username, password, email, birth, gender, regime) VALUES (:username, :password, :email, :birth, :gender, :regime)")

        # Vérification si username ou email n'existent pas déjà

        from views.users.verify_doublons import verify_doublons
        from views.users.control_password import control_password

        result = verify_doublons(sql, username, password, email, birth, gender, regime)

        return result

    def get_user(user_id=False, username=False, email=False):
        if username == False and email == False :
            user = User.query.filter_by(user_id=user_id).first()       
        elif user_id == False and email == False :
            user = User.query.filter_by(username=username).first()
        else :
            user = User.query.filter_by(email=email).first()
        return user

    def modify_user():
        pass

    def delete_user():
        pass


