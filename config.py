from flask import *
from flask_sqlalchemy import *
from passlib.hash import sha256_crypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:qwerty@localhost/hackonstack'
db = SQLAlchemy(app)
app.secret_key = 'random secret key'
