from db import db
from models import comment, friend, history, img, ingredient, like, log, notif, post, recipe_ingredient_int, recipe, signal, user
from app import app

# run "python app/models.py" pour créer le database

with app.app_context():
    db.create_all()