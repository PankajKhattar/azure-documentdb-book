from pymongo import MongoClient

client = MongoClient("<connection-string>")
collection = client.test.users

collection.create_index({"age": 1})

# Equality
print(list(collection.find({"age": 32})))

# Range
print(list(collection.find({"age": {"$gt": 25}})))