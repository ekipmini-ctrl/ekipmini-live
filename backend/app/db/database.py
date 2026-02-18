import pymongo

class MongoDB:
    def __init__(self, uri: str):
        self.client = pymongo.MongoClient(uri)
        self.db = self.client.get_default_database()

    def insert_one(self, collection_name: str, document: dict):
        collection = self.db[collection_name]
        return collection.insert_one(document)

    def find_one(self, collection_name: str, query: dict):
        collection = self.db[collection_name]
        return collection.find_one(query)

# Example usage
if __name__ == '__main__':
    mongo_db = MongoDB('your_mongodb_uri')
    # Example of inserting a document
    result = mongo_db.insert_one('test_collection', {'name': 'Test User', 'age': 30})
    print('Inserted document ID:', result.inserted_id)