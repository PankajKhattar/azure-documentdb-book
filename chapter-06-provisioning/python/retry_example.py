from pymongo import MongoClient, errors
import time
import random

client = MongoClient("<connection-string>", serverSelectionTimeoutMS=5000)

def safe_query(max_retries=5):
    for attempt in range(max_retries):
        try:
            return client.db.users.find_one()

        except (errors.AutoReconnect, errors.NetworkTimeout) as e:
            wait = (2 ** attempt) + random.uniform(0, 1)
            print(f"Retry {attempt+1}: waiting {wait:.2f}s")
            time.sleep(wait)

        except Exception as e:
            print(f"Fatal error: {e}")
            raise

    raise Exception("Failed after retries")

if __name__ == "__main__":
    print(safe_query())