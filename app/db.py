from pymongo import MongoClient

client = MongoClient('localhost', 27017, username="root", password="root")

# vamos a conectar a una db
db = client["book_store_silabuz"]
