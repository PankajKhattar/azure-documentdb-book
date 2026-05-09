from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["shop"]

stats = db.command("dbStats")

print("Collections:", stats["collections"])
print("Objects:", stats["objects"])
print("Storage Size:", stats["storageSize"])
print("Indexes:", stats["indexes"])