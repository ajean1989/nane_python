from db import db 

recipe_ingredient_int = db.Table(
    "recipe_ingredient_int",
    db.Column('id_recipe', db.Integer,db.ForeignKey('recipe.id_recipe'), unique=False, nullable=False),
    db.Column('id_ingredient', db.Integer, db.ForeignKey('ingredient.id_ingredient'), unique=False, nullable=False),

    db.Column('weight', db.Integer, unique=False, nullable=False),
)
