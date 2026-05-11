from pymongo import MongoClient
import math

client = MongoClient(
    "mongodb://localhost:27017"
)

db = client["ai"]

collection = db["products"]

target_product = collection.find_one({
    "_id": "p101"
})

target_embedding = target_product["embedding"]

def similarity(vec1, vec2):

    dot = sum(a * b for a, b in zip(vec1, vec2))

    mag1 = math.sqrt(
        sum(a * a for a in vec1)
    )

    mag2 = math.sqrt(
        sum(b * b for b in vec2)
    )

    return dot / (mag1 * mag2)

recommendations = []

for product in collection.find():

    if product["_id"] == "p101":
        continue

    score = similarity(
        target_embedding,
        product["embedding"]
    )

    recommendations.append({
        "product": product["name"],
        "score": score
    })

recommendations.sort(
    key=lambda x: x["score"],
    reverse=True
)

print("Recommended Products")

for item in recommendations[:5]:

    print(item)
