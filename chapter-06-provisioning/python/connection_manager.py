from pymongo import MongoClient

class MongoConnectionManager:
    def __init__(self, uri):
        self.client = MongoClient(
            uri,
            maxPoolSize=50,
            minPoolSize=5,
            serverSelectionTimeoutMS=5000
        )

    def get_db(self, db_name):
        return self.client[db_name]

    def health_check(self):
        try:
            self.client.admin.command("ping")
            return True
        except Exception:
            return False