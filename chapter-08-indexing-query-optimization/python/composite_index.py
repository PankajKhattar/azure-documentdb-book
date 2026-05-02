from pymongo import MongoClient

client = MongoClient("<connection-string>")
collection = client.test.orders

collection.create_index([
    ("customerId", 1),
    ("orderDate", -1)
])

# Supported query (prefix + sort)
result = collection.find({
    "customerId": "C123"
}).sort("orderDate", -1)

print(list(result))

# Full query with range
result = collection.find({
    "customerId": "C123",
    "orderDate": {"$gte": "2025-01-01"}
})

print(list(result))