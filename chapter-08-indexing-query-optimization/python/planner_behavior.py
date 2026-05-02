from pymongo import MongoClient
import pprint

client = MongoClient("<connection-string>")
collection = client.test.orders

query = {"customerId": "C123"}

explain = collection.find(query).explain("executionStats")

pprint.pprint({
    "executionTimeMillis": explain["executionStats"]["executionTimeMillis"],
    "totalDocsExamined": explain["executionStats"]["totalDocsExamined"],
    "totalKeysExamined": explain["executionStats"]["totalKeysExamined"]
})