import time
from pymongo import MongoClient
from pymongo.errors import AutoReconnect

client = MongoClient(
    "mongodb://localhost:27017",
    serverSelectionTimeoutMS=3000
)

db = client["shop"]
collection = db["orders"]

MAX_RETRIES = 3

def get_order(order_id):

    for attempt in range(MAX_RETRIES):

        try:

            print(f"Attempt {attempt + 1}")

            result = collection.find_one({
                "_id": order_id
            })

            return result

        except AutoReconnect:

            print("Transient failure detected")
            time.sleep(1)

    raise Exception("Operation failed after retries")

try:

    order = get_order("order_101")

    print("Query result:")
    print(order)

except Exception as err:

    print("Error:", err)