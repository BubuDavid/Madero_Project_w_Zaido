from pymongo import MongoClient

MONGO_URI = "mongodb+srv://user:password@cluster0-mwb3d.mongodb.net/test?retryWrites=true&w=majority"

def db_connect(MONGO_URI, db_name, col_name):
    client = MongoClient(MONGO_URI)
    database = client[db_name]
    collection = database[col_name]
    return collection


def db_insert_user(collection, user):
    return collection.insert_one(user)


def db_find_all(collection, query={}):
    return collection.find(query)

def db_delete_one(collection, query={}):
	return collection.delete_many(query)
