from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017")

db = client.bookdb
users = db.users

users.insert_one({
    "userId": "u123",
    "name": "Alice",
    "preferences": {
        "language": "en",
        "notifications": True
    },
    "createdAt": datetime.utcnow()
})

print("Document inserted successfully")
