from flask_wtf import FlaskForm
from wtforms import StringField, SelectField,PasswordField, EmailField, DateField,FileField
from wtforms.validators import DataRequired, length, Regexp, Email


class RegisterForm(FlaskForm):
    username= StringField('username', validators=[DataRequired(message='Vous devez remplir le champ "Username".'), length(min=2, max=32, message='Le nom d\'utilisateur doit faire entre 2 et 32 caractères.')])
    email = EmailField('email', validators=[DataRequired(message='Vous devez remplir le champ "e-mail".'),Regexp("^[\w.-]+@[a-zA-Z_-]+?(?:\.[a-zA-Z]{2,6})+$", message="L'adresse mail n'est pas conforme")])
    password = PasswordField('password', validators=[DataRequired(message='Vous devez remplir le champ "Mot de passe".'), length(8,32, message="Le mot de passe doit contenir entre 8 et 32 caractères."), Regexp("^(?=.*\d)(?=.*[A-Z])", message='Le mot de passe doit comporter au moins un chiffre et une majuscule')])
    birth = DateField('birth', validators=[DataRequired(message='Vous devez remplir le champ "Date de naissance".')])
    gender = SelectField('gender', choices=[('M','Homme'),('F','Femme'),('O','Autre')])
    regime = SelectField('regime', choices=[('A','Je mange de tout'),('V','Végétarien'),('VG','Vegan')])
    avatar = FileField('avatar')

