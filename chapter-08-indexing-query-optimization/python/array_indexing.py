from pymongo import MongoClient

client = MongoClient("<connection-string>")
collection = client.test.users

collection.insert_one({
    "_id": "u1",
    "tags": ["premium", "active", "beta"]
})

collection.create_index({"tags": 1})

# Membership query
result = collection.find({"tags": "premium"})

print(list(result))