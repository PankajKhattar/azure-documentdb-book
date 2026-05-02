from pymongo import MongoClient

client = MongoClient("<connection-string>")
collection = client.test.users

collection.insert_one({
    "_id": "u1",
    "profile": {
        "age": 32,
        "city": "Delhi"
    }
})

# Index on nested path
collection.create_index("profile.age")

# Query using nested path
result = collection.find({"profile.age": 32})

print(list(result))