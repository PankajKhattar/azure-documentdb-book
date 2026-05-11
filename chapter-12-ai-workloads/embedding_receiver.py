from pymongo import MongoClient

client = MongoClient(
    "mongodb://localhost:27017"
)

db = client["ai"]

collection = db["documents"]

print("Starting embedding listener...")

change_stream = collection.watch()

for change in change_stream:

    if change["operationType"] == "insert":

        document = change["fullDocument"]

        print("=================================")
        print("New document detected")
        print(document)

        # Simulated embedding generation

        embedding = [
            0.12,
            -0.44,
            0.91,
            0.33
        ]

        collection.update_one(
            {
                "_id": document["_id"]
            },
            {
                "$set": {
                    "embedding": embedding
                }
            }
        )

        print("Embedding stored")
