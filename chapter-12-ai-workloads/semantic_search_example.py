from pymongo import MongoClient
import math

client = MongoClient(
    "mongodb://localhost:27017"
)

db = client["ai"]

collection = db["documents"]

# Simulated query embedding

query_embedding = [
    0.10,
    -0.40,
    0.88,
    0.31
]

def cosine_similarity(vec1, vec2):

    dot_product = sum(a * b for a, b in zip(vec1, vec2))

    norm_vec1 = math.sqrt(
        sum(a * a for a in vec1)
    )

    norm_vec2 = math.sqrt(
        sum(b * b for b in vec2)
    )

    return dot_product / (
        norm_vec1 * norm_vec2
    )

results = []

for doc in collection.find({

    "embedding": {
        "$exists": True
    }

}):

    similarity = cosine_similarity(
        query_embedding,
        doc["embedding"]
    )

    results.append({
        "title": doc["title"],
        "similarity": similarity
    })

results.sort(
    key=lambda x: x["similarity"],
    reverse=True
)

print("Semantic Search Results")

for result in results:

    print(result)
