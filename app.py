from flask import *
from flask_sqlalchemy import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:qwerty@localhost/hackonstack'
db = SQLAlchemy(app)
app.secret_key = 'random secret key'

#### MODELS

class User(db.Model):
    __tablename__ = "users"
    u_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), nullable=False)
    phoneno = db.Column(db.String(13))
    bio = db.Column(db.String(1000))
    dob = db.Column(db.DateTime, nullable=False)

class Question(db.Model):
    __tablename__ = "questions"
    q_id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text)
    author_u_id = db.Column(db.Integer, nullable=False)
    post_time = db.Column(db.DateTime, nullable=False)
    upvotes = db.Column(db.Integer)
    # upvoters_id = ??

class Answers(db.Model):
    __tablename__ = "answers"
    a_id = db.Column(db.Integer, primary_key=True, nullable=False)
    q_id = db.Column(db.Integer, nullable=False)
    body = db.Column(db.Text)
    author_u_id = db.Column(db.Integer)
    post_time = db.Column(db.DateTime)
    upvotes = db.Column(db.Integer)

db.create_all()

#### ROUTES

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/login/', methods=['POST','GET'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        pass

@app.route('/register/', methods=['POST','GET'])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        pass

@app.route('/post/question/', methods=['POST','GET'])
def post_question():
    if request.method == "GET":
        return render_template("ask_question.html")
    else:
        pass

@app.route('/post/answer/', methods=['POST'])
def post_answer():
    pass

@app.route('/question/<int:q_id>')
def question(q_id):
    return render_template("display_question.html")

@app.route('/upvote/question/<int:q_id>/', methods=['POST'])
def upvote_q(q_id):
    pass

@app.route('/downvote/question/<int:q_id>/', methods=['POST'])
def downvote_q(q_id):
    pass

@app.route('/upvote/answer/<int:a_id>/', methods=['POST'])
def upvote_a(a_id):
    pass

@app.route('/downvote/answer/<int:a_id>/', methods=['POST'])
def downvote_a(a_id):
    pass

@app.route('/profile/<int:u_id>/')
def function(u_id):
    return render_template("profile.html")

if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0',80)
