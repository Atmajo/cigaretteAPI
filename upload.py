import json
from pymongo import MongoClient

# Define the MongoDB connection settings
mongo_uri = "mongodb+srv://ecommerce:boom1234@cluster0.wrhg7tc.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp"  # Replace with your MongoDB URI
database_name = "cigarette"  # Replace with your database name
collection_name = "cigaretteData"  # Replace with your collection name

# Connect to MongoDB
client = MongoClient(mongo_uri)
db = client[database_name]
collection = db[collection_name]


def insert_json_data(jfile):
    with open(jfile, 'r') as file:
        data = json.load(file)
        collection.insert_many(data)


json_files = ["cigarettes.json"]

# Upload each JSON file to MongoDB
for json_file in json_files:
    insert_json_data(json_file)

# Close the MongoDB connection
client.close()
