import pymongo

# Connect to mongodb
myclient = pymongo.MongoClient("mongodb://localhost:27017/",username='root',password='example')
