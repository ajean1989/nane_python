from db import db 


class Friend(db.Model):
    id_friend = db.Column(db.Integer, primary_key=True)
    list_friends = db.Column(db.JSON, unique=False, nullable=True)
    id_user = db.Column(db.Integer, unique=True, nullable=False)

    def create_friend(username, password, email, birth, gender, regime):
        pass

    def get_friend_list(user_id=False, username=False, email=False):
        pass

    def delete_friend():
        pass
