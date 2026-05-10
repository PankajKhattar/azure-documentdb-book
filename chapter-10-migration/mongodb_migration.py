from pymongo import MongoClient

SOURCE_URI = "mongodb://localhost:27017"
TARGET_URI = "mongodb://localhost:27018"

source_client = MongoClient(SOURCE_URI)
target_client = MongoClient(TARGET_URI)

source_db = source_client["shop"]
target_db = target_client["shop"]

source_collection = source_db["orders"]
target_collection = target_db["orders"]

print("Starting MongoDB migration...")

count = 0

for document in source_collection.find(batch_size=1000):

    target_collection.insert_one(document)

    count += 1

    if count % 1000 == 0:
        print(f"Migrated {count} documents")

print("Migration completed")
print(f"Total migrated documents: {count}")