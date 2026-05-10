from pymongo import MongoClient
import time

client = MongoClient(
    "mongodb://localhost:27017"
)

db = client["shop"]
collection = db["users"]

cache = {}

CACHE_TTL = 10

def get_user(user_id):

    current_time = time.time()

    if user_id in cache:

        cached_data = cache[user_id]

        if current_time - cached_data["timestamp"] < CACHE_TTL:

            print("Cache HIT")

            return cached_data["data"]

    print("Cache MISS")

    user = collection.find_one({
        "_id": user_id
    })

    cache[user_id] = {
        "data": user,
        "timestamp": current_time
    }

    return user

print(get_user("user_101"))
print(get_user("user_101"))