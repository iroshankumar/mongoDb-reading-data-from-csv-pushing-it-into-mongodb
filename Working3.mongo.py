import pandas as pd
import pymongo

# Connect to MongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
print(myclient.list_database_names())

# Specify the database name
mydb = myclient["test3"]

# Check if the database exists
dblist = myclient.list_database_names()

# Read data from CSV file into a DataFrame
df = pd.read_csv("titanic.csv")

# Convert DataFrame to dictionary format
data = df.to_dict(orient="records")

# Specify the collection name
collection = mydb["Titanic"]
print(collection)

# Insert data into MongoDB collection
#collection.insert_many(data)

# Find documents in the collection
documents = collection.find()
for doc in documents:
    print(doc)
