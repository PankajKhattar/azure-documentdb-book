import time
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

collection = client.db.orders

start = time.time()

for _ in range(1000):
    collection.find_one({"customerId": "C123"})

print("Elapsed:", time.time() - start)