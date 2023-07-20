
# database

username = 'root'
mdp = 'adrien'
db_name = 'nane'

SECRET_KEY='dev',
SQLALCHEMY_DATABASE_URI=f"mysql://{username}:{mdp}@mysql:3306/{db_name}"

# Sécurity

#SECURITY_DEFAULT_REMEMBER_ME = False
SECURITY_LOGIN_URL = '/log'