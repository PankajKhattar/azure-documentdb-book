from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["banking"]

customers = db["customers"]

customer = {
    "_id": "C123",
    "name": "John Smith",
    "accounts": [
        {
            "type": "Savings",
            "balance": 5000
        },
        {
            "type": "Credit Card",
            "limit": 10000
        }
    ],
    "riskScore": 78
}

customers.insert_one(customer)

profile = customers.find_one({
    "_id": "C123"
})

print(profile)