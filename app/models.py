# from db import db

# class Coms(db.Model):
#     com_id = db.Column(db.Integer, unique=True, nullable=False)
#     content = db.Column(db.String, unique=False, nullable=False)
#     response_com_id = db.Column(db.Integer, unique=False, nullable=True)
#     recipe_id = db.Column(db.Integer, unique=False, nullable=False)
#     post_id = db.Column(db.Integer, unique=False, nullable=True)


# class Friends(db.Model):
#     user_id = db.Column(db.Integer, unique=False, nullable=True)
#     users_id = db.Column(db.JSON, unique=False, nullable=True)

# class Images(db.Model):
#     image_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.Float, unique=False, nullable=False)
#     type = db.Column(db.Integer, unique=False, nullable=False)

# class Ingredients(db.Model):
#     ingredient_id = db.Column(db.Integer, primary_key=True)
#     recipe_id = db.Column(db.String, unique=False, nullable=True)
#     name = db.Column(db.String, unique=True, nullable=False)

# class Likes(db.Model):
#     like_id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, unique=False, nullable=False)
#     recipe_id = db.Column(db.Integer, unique=False, nullable=True)
#     com_id = db.Column(db.Integer, unique=False, nullable=True)
#     post_id = db.Column(db.Integer, unique=False, nullable=True)


# class News(db.Model):
#     user_id = db.Column(db.Integer, unique=False, nullable=False)
#     recipes_id = db.Column(db.JSON, unique=False, nullable=False)
#     posts_id = db.Column(db.JSON, unique=False, nullable=False)


# class Notifications(db.Model):
#     notification_id  = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, unique=False, nullable=False)
#     recipe_id = db.Column(db.Integer, unique=False, nullable=True)
#     like_id = db.Column(db.Integer, unique=False, nullable=True)
#     com_id = db.Column(db.Integer, unique=False, nullable=True)
#     type = db.Column(db.Integer, unique=False, nullable=False)
#     status = db.Column(db.Integer, unique=False, nullable=False)

# class Recipes(db.Model):
#     recipe_id = db.Column(db.Integer, primary_key=True)
#     image_id = db.Column(db.Integer, unique=True, nullable=True)
#     intro = db.Column(db.String, unique=False, nullable=False)
#     name = db.Column(db.String, unique=False, nullable=False)
#     type = db.Column(db.Integer, unique=False, nullable=False)
#     quantity = db.Column(db.Integer, unique=False, nullable=False)
#     video = db.Column(db.String, unique=False, nullable=True)
#     date = db.Column(db.TIMESTAMP, unique=False, nullable=False)
#     modification_date = db.Column(db.DateTime, unique=False, nullable=True)
#     status = db.Column(db.Integer, unique=False, nullable=False)
#     regime = db.Column(db.Integer, unique=False, nullable=False)


# class Steps(db.Model):
#     recipe_id = db.Column(db.Integer, primary_key=True)
#     image_id = db.Column(db.Integer, unique=False, nullable=True)
#     number = db.Column(db.Integer, unique=False, nullable=False)
#     description = db.Column(db.String, unique=False, nullable=False)

# class Users(db.Model):
#     user_id = db.Column(db.Integer, primary_key=True)
#     image_id = db.Column(db.Integer, unique=True, nullable=False)
#     email = db.Column(db.String, unique=True, nullable=False)
#     username = db.Column(db.String, unique=True, nullable=False)
#     password = db.Column(db.String, unique=False, nullable=False)
#     birth = db.Column(db.DateTime, unique=False, nullable=False)
#     gender = db.Column(db.Integer, unique=False, nullable=False)
#     regime = db.Column(db.Integer, unique=False, nullable=False)
#     status = db.Column(db.Integer, unique=False, nullable=False)

# class Views(db.Model):
#     recipe_id = db.Column(db.Integer, unique=False, nullable=False)
#     view = db.Column(db.Integer, unique=False, nullable=False)

# class Weight(db.Model):
#     recipe_id = db.Column(db.Integer, unique=False, nullable=False)
#     ingredient_id = db.Column(db.Integer, unique=False, nullable=False)
#     weight = db.Column(db.Integer, unique=False, nullable=False)

# class Posts(db.Model):
#     post_id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, unique=False, nullable=False)
#     content = db.Column(db.String, unique=False, nullable=True)
#     image_id = db.Column(db.Integer, unique=False, nullable=True)

# class Log(db.Model):
#     user_id = db.Column(db.Integer, unique=False, nullable=False)
#     date = db.Column(db.DateTime, unique=False, nullable=False)
#     seen_user_id = db.Column(db.Integer, unique=False, nullable=True)
#     seen_recipe_id = db.Column(db.Integer, unique=False, nullable=True)
#     seen_post_id = db.Column(db.Integer, unique=False, nullable=True)
