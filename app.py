from flask import *

app = Flask(__name__)
app.secret_key = 'random secret key'

@app.route('/')
def homepage():
    pass

@app.route('/login/', methods=['POST','GET'])
def login():
    pass

@app.route('/register/', methods=['POST','GET'])
def register():
    pass

@app.route('/post/question/', methods=['POST','GET'])
def post_question():
    pass

@app.route('/post/answer/', methods=['POST'])
def post_answer():
    pass

@app.route('/question/<int:q_id>')
def question(q_id):
    pass

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
    pass

if __name__ == '__main__':
    app.debug = True
    app.run()
