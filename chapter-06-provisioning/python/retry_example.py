from pymongo import MongoClient, errors
import time
import random

client = MongoClient("mongodb://localhost:27017", serverSelectionTimeoutMS=5000)

def safe_query(max_retries=5):
    for attempt in range(max_retries):
        try:
            return client.db.users.find_one()

        except (errors.AutoReconnect, errors.NetworkTimeout) as e:
            wait_time = (2 ** attempt) + random.uniform(0, 1)
            print(f"[Retry {attempt+1}] Transient error: {e}, retrying in {wait_time:.2f}s")
            time.sleep(wait_time)

        except Exception as e:
            print(f"Non-retryable error: {e}")
            raise

    raise Exception("Operation failed after retries")

if __name__ == "__main__":
    result = safe_query()
    print(result)