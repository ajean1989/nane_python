import os

import sys
print(sys.path)
# Flask + SQLAlchemy

from flask import Flask, render_template, request, session

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')

# Autres dossiers

from models.users import *


# Flask WTF

from flask_wtf import CSRFProtect
csrf = CSRFProtect(app)

# App 

@app.route('/')
def main():
    return render_template('main.html')

@app.get('/register')
def register_get():
    from views.forms.register import RegisterForm
    form=RegisterForm()
    return render_template('register.html',form=form)

@app.route('/register', methods=['GET','POST'])
def register_post():
     # Déjà connecté
    try: 
        if session['username'] in globals(): 
            return render_template('main.html')
    except:
        pass

    # Sinon
    from views.forms.register import RegisterForm
    form=RegisterForm()

    if request.method == 'GET' :
        return render_template('register.html',form=form)

    else :
        if form.validate_on_submit():
            result = User.create_user(form.username.data,form.password.data,form.email.data,form.birth.data,form.gender.data,form.regime.data)
            if result == 'Enregistrement effectué':
                session['flash']='Enregistrement effectué'
                session['temp_user']=form.username.data
                return redirect('/login')
            else:
                return render_template('register.html', result=result, form=form)
        else : 
            result=''
            for value in form.errors.values():
                result=str(value[0]) #str values pour l'affichage, sinon liste
            test = None
            return render_template('register.html', result=result, test=test, form=form)


@app.route('/login', methods=['GET','POST'])
def sign_post():
    # Déjà connecté
    try: 
        if session['username'] in globals(): 
            return render_template('main.html')
    except:
        pass

    # Sinon
    from views.forms.login import LoginForm

    form=LoginForm()

    if request.method == 'GET' :
        return render_template('login.html', form=form)
    else :
        from passlib.hash import argon2

        # Vérification password
        user = User.get_user(username=request.form['username'])
        db_password = user.password
        input_password = form.password.data

        if argon2.verify(input_password, db_password) :
            import secrets
            session['username'] = user.username
            session['token']=secrets.token_hex(32) ## Faire du JWT ou nouvel attribut token dans bdd
            test = 'log !'
            return redirect('/')
        else : 
            return render_template('login.html', form=form)

@app.get('/logout')
def logout():
    session['username'] = False
    return render_template('layout.html')


@app.get('/test')
def test():
    return render_template('test.html')

#API 

# @app.post('/api/register')
# def api_register_post():

#     from views.forms.register import RegisterForm
#     form=RegisterForm()

#     if form.validate_on_submit():
#             result = User.create_user(form.username.data,form.password.data,form.email.data,form.birth.data,form.gender.data,form.regime.data)
#             test = None
#             return {'test':'nok'}
#     else : 
#         result=''
#         for value in form.errors.values():
#             result=str(value[0]) #str values pour l'affichage, sinon liste
#         test = None
#         return {'test':'ok'}