from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["retail"]

products = db["products"]

product = {
    "_id": "P1001",
    "name": "Gaming Laptop",
    "category": "Electronics",
    "price": 1499,
    "specifications": {
        "cpu": "Intel Core i9",
        "memory": "32GB",
        "storage": "1TB SSD"
    }
}

products.insert_one(product)

print("Product inserted")

result = products.find_one({
    "category": "Electronics"
})

print(result)