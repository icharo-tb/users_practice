import pymongo
import pprint
from password_hash import hash_password

conn = pymongo.MongoClient('mongodb://localhost:27017/')
db = conn['Fake_Users']
collection = db['users']

pprint.pprint(collection.find({'password':{'$exists': True}}))