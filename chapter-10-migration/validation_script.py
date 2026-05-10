from pymongo import MongoClient

SOURCE_URI = "mongodb://localhost:27017"
TARGET_URI = "mongodb://localhost:27018"

source_client = MongoClient(SOURCE_URI)
target_client = MongoClient(TARGET_URI)

source_db = source_client["shop"]
target_db = target_client["shop"]

source_count = source_db.orders.count_documents({})
target_count = target_db.orders.count_documents({})

print("=================================")
print("Migration Validation Report")
print("=================================")

print(f"Source document count : {source_count}")
print(f"Target document count : {target_count}")

if source_count == target_count:
    print("Validation PASSED")
else:
    print("Validation FAILED")