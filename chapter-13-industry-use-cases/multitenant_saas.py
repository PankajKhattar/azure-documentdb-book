from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["saas"]

users = db["users"]

users.insert_one({
    "tenantId": "tenantA",
    "userId": "user001",
    "name": "Alice"
})

users.insert_one({
    "tenantId": "tenantB",
    "userId": "user002",
    "name": "Bob"
})

tenant_a_users = users.find({
    "tenantId": "tenantA"
})

for user in tenant_a_users:
    print(user)