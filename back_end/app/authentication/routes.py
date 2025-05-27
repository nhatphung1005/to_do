from . import app
from flask import request, jsonify
from app.database.user import create_user, get_user_by_email
from bcrypt import hashpw, gensalt

@app.route("/register", methods=["POST"])
def register():
    username = request.json.get("username")
    password = request.json.get("password")

    try:
        from .utils import register
        register(username, password)
        return jsonify({"message": "User created successfully"}), 201
    except ValueError as e:
        return jsonify({"message": str(e)}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 400


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    try:
        from .utils import login
        user = login(username, password)
        return jsonify({"message": "User logged in successfully"}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    

