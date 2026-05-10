from pymongo import MongoClient
import threading

client = MongoClient(
    "mongodb://localhost:27017",
    maxPoolSize=50,
    minPoolSize=10
)

db = client["shop"]
collection = db["orders"]

def worker(thread_id):

    result = collection.find_one({
        "customerId": "C123"
    })

    print(f"Thread {thread_id} completed")

threads = []

for i in range(20):

    thread = threading.Thread(
        target=worker,
        args=(i,)
    )

    threads.append(thread)

    thread.start()

for thread in threads:
    thread.join()

print("All threads completed")