from models.Users import User

def get_username(u_id):
    u = User.query.filter_by(u_id=u_id).first()
    if u:
        return u.username
    else:
        return "unknown user"
