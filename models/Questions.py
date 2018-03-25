from config import db

class Question(db.Model):
    __tablename__ = "questions"
    q_id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text)
    author_u_id = db.Column(db.Integer, nullable=False)
    post_time = db.Column(db.DateTime, nullable=False)
    upvotes = db.Column(db.Integer)
    upvoters = db.Column(db.Text)
    reports = db.Column(db.Integer)
