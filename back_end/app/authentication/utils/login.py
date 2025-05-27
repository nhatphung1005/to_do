from app.database.user import get_user_by_email
from bcrypt import hashpw, gensalt

def login(username, password):
    user = get_user_by_email(username)
    if not user:
        raise ValueError("User not found")
    
    if not hashpw(password.encode("utf-8"), user["password"]):
        raise ValueError("Invalid password")
    
    return user