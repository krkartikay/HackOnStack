from config import *
from app import app

db.create_all()

if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0',80)
