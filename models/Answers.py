from config import db

class Answer(db.Model):
    __tablename__ = "answers"
    a_id = db.Column(db.Integer, primary_key=True, nullable=False)
    q_id = db.Column(db.Integer, nullable=False)
    body = db.Column(db.Text)
    author_u_id = db.Column(db.Integer)
    post_time = db.Column(db.DateTime)
    upvotes = db.Column(db.Integer)
