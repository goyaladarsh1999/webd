import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://goyaladarsh1999:Aars#3709@goyaladarsh1999.xloy0.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["test"]
collection = db["test"]

post = {"_id": 1, "name": "tim",  "score": 5} #if id not mentioned then a random id will be created

collection.insert_one(post)