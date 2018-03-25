from config import *
from app import app
import helpers

app.jinja_env.globals.update(helpers=helpers)

db.create_all()

if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0',80)
