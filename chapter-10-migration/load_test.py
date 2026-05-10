import time
from pymongo import MongoClient

TARGET_URI = "mongodb://localhost:27018"

client = MongoClient(TARGET_URI)

db = client["shop"]

collection = db["orders"]

print("Starting load test...")

start_time = time.time()

for i in range(1000):

    collection.find_one({
        "customerId": "C123"
    })

end_time = time.time()

print("=================================")
print("Load Test Results")
print("=================================")

print(f"Total execution time: {end_time - start_time:.2f} seconds")
print(f"Queries executed: 1000")