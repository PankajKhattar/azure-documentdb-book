from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017")

db = client["iot"]

telemetry = db["telemetry"]

document = {
    "deviceId": "sensor-101",
    "timestamp": datetime.utcnow(),
    "temperature": 24.8,
    "humidity": 56
}

telemetry.insert_one(document)

print("Telemetry stored")