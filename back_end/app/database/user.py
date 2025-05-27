from .connection import db
import re
from bcrypt import hashpw, gensalt

def create_user(user):
    #check user already exists
    if db.users.find_one({"email": user["email"]}):
        raise ValueError("User already exists")
        raise Exception("User already exists")


    #check for mat
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", user["email"]):
        raise ValueError("Invalid email")

    db.users.insert_one(user)

def get_user(user_id):
    return db.users.find_one({"_id": user_id})

def get_user_by_email(email):
    return db.users.find_one({"email": email})

def update_user(user_id, user):
    db.users.update_one({"_id": user_id}, {"$set": user})