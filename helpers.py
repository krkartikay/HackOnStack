from models.Users import User
from mistune import markdown

def get_username(u_id):
    u = User.query.filter_by(u_id=u_id).first()
    if u:
        return u.username
    else:
        return "unknown user"

def get_top_users():
    u = User.query.order_by(User.reputation.desc()).all()
    return u
