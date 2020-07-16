import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://goyaladarsh1999:<password>@goyaladarsh1999.xloy0.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = cluster["test"]
collection = db["test"]

post = {"_id":5, "name": "tim"} #if id not mentioned then a random id will be created

collection.insert_one(post)