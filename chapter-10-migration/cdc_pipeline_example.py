from pymongo import MongoClient

SOURCE_URI = "mongodb://localhost:27017"
TARGET_URI = "mongodb://localhost:27018"

source_client = MongoClient(SOURCE_URI)
target_client = MongoClient(TARGET_URI)

source_db = source_client["shop"]
target_db = target_client["shop"]

collection = source_db["orders"]

print("Starting CDC pipeline listener...")

change_stream = collection.watch()

for change in change_stream:

    print("=================================")
    print("Change detected")
    print(change)

    if change["operationType"] == "insert":

        document = change["fullDocument"]

        target_db.orders.insert_one(document)

        print("Document replicated to target")