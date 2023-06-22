from pymongo import MongoClient

# Create a MongoClient object.
client = MongoClient('mongodb', 27017)
db = client.flask_db
repo_db = db.repo_db