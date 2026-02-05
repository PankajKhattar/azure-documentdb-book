from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://bookuser:bookpassword@localhost:10260/?authSource=admin&tls=true&tlsAllowInvalidCertificates=true")

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
