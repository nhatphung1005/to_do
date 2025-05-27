from flask import Blueprint, request, jsonify

app = Blueprint("authentication", __name__)

url_prefix = "/api/authentication"