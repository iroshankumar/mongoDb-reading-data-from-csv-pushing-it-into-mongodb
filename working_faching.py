from pymongo import MongoClient

class Mdb():
    def __init__(self, DatabaseName):
        self.client = MongoClient("localhost", 27017)
        self.db = self.client[DatabaseName]
        print("Connected to and using database: {}".format(DatabaseName))

    def show_collections(self):
        collections = self.db.list_collection_names()
        print("The list of collections are:")
        for col in collections:
            print(col)

    def insert_one(self, collection_name, data):
        collection = self.db[collection_name]
        return collection.insert_one(data)

    def insert_many(self, collection_name, data):
        collection = self.db[collection_name]
        return collection.insert_many(data)

    def update_one(self, collection_name, query, update):
        collection = self.db[collection_name]
        return collection.update_one(query, {'$set': update})

    def find_one(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.find_one(query)

    def delete_one(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.delete_one(query)


# Example usage:
if __name__ == "__main__":
    # Connect to MongoDB
    mongo = Mdb("rahul1")

    # Inserting a document
    document = {"name": "rahul ", "age": 30}
    result = mongo.insert_one("users", document)
    print("Inserted document ID:", result.inserted_id)

    # Finding a document
    query = {"name": "John"}
    found_document = mongo.find_one("users", query)
    print("Found document:", found_document)

    # Updating a document
    update_query = {"name": "John"}
    update_data = {"age": 35}
    update_result = mongo.update_one("users", update_query, update_data)
    print("Updated document:", update_result.modified_count)

    # Deleting a document
    delete_query = {"name": "John"}
    delete_result = mongo.delete_one("users", delete_query)
    print("Deleted document:", delete_result.deleted_count)

    # Showing collections
    mongo.show_collections()
