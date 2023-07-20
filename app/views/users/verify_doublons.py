from models.users import User
from db import db 

def verify_doublons(sql, username, password, email, birth, gender, regime): 
    
    if User.get_user(email=email) != None :
        result = 'Cette adresse mail a déjà été utilisée.'
        return result
    elif User.get_user(username=username) != None :
        result = 'Ce nom existe déjà.'
        return result
    else :
        from passlib.hash import argon2
        password = argon2.hash(password)
        db.session.execute(sql, {"username": username, "password": password, "email": email, "birth": birth, "gender": gender, "regime": regime})
        db.session.commit()
        result = 'Enregistrement effectué'
        return result

