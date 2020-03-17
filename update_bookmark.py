import pymongo

from urllib.parse import urlparse

client =  pymongo.MongoClient("mongodb://localhost:27017/")

db = client.bookmarks
collection = db.bookmark

parent = collection.find({'parent_id':0})

data = list(parent)

for d in data:
    
    children = collection.find({'parent_id':d['_id']})
    datas = list(children)

    for c in datas:

        myquery = { "_id": c['_id'] }

        url = c['href']

        info = urlparse(url)

        icon = info.scheme + "://" + info.netloc + "/favicon.ico"

        newvalues = { "$set": { "icon": icon } }

        collection.update_one(myquery,newvalues)
