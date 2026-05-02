from pymongo import MongoClient

client = MongoClient("<connection-string>")
collection = client.test.articles

collection.insert_many([
    {"_id": "a1", "keywords": ["distributed", "database", "scaling"]},
    {"_id": "a2", "keywords": ["database", "indexing"]}
])

# Multi-term containment query
result = collection.find({
    "keywords": {"$all": ["distributed", "scaling"]}
})

print(list(result))