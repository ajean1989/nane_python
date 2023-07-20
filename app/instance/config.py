
# database

username = 'adrien'
mdp = 'adr13NjMy'
db_name = 'nane'

SECRET_KEY='dev',
SQLALCHEMY_DATABASE_URI=f"mysql://{username}:{mdp}@localhost:3306/{db_name}"

# Sécurity

#SECURITY_DEFAULT_REMEMBER_ME = False
SECURITY_LOGIN_URL = '/log'