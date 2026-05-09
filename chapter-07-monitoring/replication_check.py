from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

status = client.admin.command("serverStatus")

print("Connections:", status["connections"])
print("Uptime:", status["uptime"])