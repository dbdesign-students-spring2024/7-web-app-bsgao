from pymongo import MongoClient

try:
    client = MongoClient('mongodb://admin:5um2UPES@class-mongodb.cims.nyu.edu:27017/admin?authSource=admin')
    db = client.admin
    result = db.command("ping")
    print("Connection successful:", result)
except Exception as e:
    print("Error connecting to MongoDB:", e)
