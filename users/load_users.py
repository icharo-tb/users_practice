import pymongo
import sqlite3
import json

# MongoDB connection
conn = pymongo.MongoClient('mongodb://localhost:27017/')
db = conn['Fake_Users']
collection = db['users']

with open('user.json','r') as f:
    json_file = json.load(f)
    
collection.insert_one(json_file)