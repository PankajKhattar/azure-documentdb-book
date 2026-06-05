from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["healthcare"]

patients = db["patients"]

patient = {
    "_id": "PAT1001",
    "name": "Jane Doe",
    "allergies": [
        "Penicillin"
    ],
    "medications": [
        {
            "name": "Aspirin",
            "dosage": "100mg"
        }
    ],
    "diagnoses": [
        {
            "condition": "Hypertension",
            "date": "2025-01-15"
        }
    ]
}

patients.insert_one(patient)

record = patients.find_one({
    "_id": "PAT1001"
})

print(record)