#from pymongo import MongoClient
import pymongo

#client = MongoClient("mongodb+srv://dreamfly:1qaz2wsx@cluster0-7eeqx.mongodb.net/test?retryWrites=true&w=majority")


#client = pymongo.MongoClient("mongodb+srv://dreamfly:1qaz2wsx@cluster0-7eeqx.mongodb.net/test?retryWrites=true&w=majority")
#db = client.test
client = pymongo.MongoClient("mongodb://localhost:27017/")


db = client.bookmarks


collection = db.bookmark


print(collection)

data = {
    "title":"谷歌",
    "href":"https://www.google.com/",
    "icon":'https://www.google.com/favicon.ico',
    "desc":"as fast as you can"
}

#inserted_id = collection.insert_one(data).inserted_id

print(collection.find_one({"title":"谷歌"}))

#print(inserted_id)