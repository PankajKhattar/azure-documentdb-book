from pymongo import MongoClient

client = MongoClient("<connection-string>")
collection = client.test.orders

# Query WITHOUT shard key
result = collection.find({
    "amount": {"$gt": 10000}
})

print(list(result))