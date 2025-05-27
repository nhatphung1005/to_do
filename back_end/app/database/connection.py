from pymongo import MongoClient

client = MongoClient("mongodb://root:root@db:27017/")

db = client["production"]

