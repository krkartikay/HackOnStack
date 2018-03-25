from config import db

class User(db.Model):
    __tablename__ = "users"
    u_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(77))
    email = db.Column(db.String(80), nullable=False)
    phone_no = db.Column(db.String(13))
    bio = db.Column(db.String(1000))
    dob = db.Column(db.DateTime, nullable=False)
    reputation = db.Column(db.Integer, default=100)
