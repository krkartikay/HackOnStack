from flask import *

app = Flask(__name__)
app.secret_key = 'random secret key'

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
def upvote_q(a_id):
    pass

@app.route('/downvote/answer/<int:a_id>/', methods=['POST'])
def downvote_q(a_id):
    pass

@app.route('/profile/<int:u_id>/')
def function(u_id):
    return render_template("profile.html")

if __name__ == '__main__':
    app.debug = True
    app.run()
