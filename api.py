import pymongo

from urllib.parse import urlparse
from urllib.parse import parse_qs
from http.server import HTTPServer, BaseHTTPRequestHandler
from bson.json_util import dumps
from bson.objectid import ObjectId

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.bookmarks
collection = db.bookmark

parent = collection.find({'parent_id':0})

data = list(parent)

for d in data:
    children = collection.find({'parent_id':d['_id']})
    datas = list(children)
    d['children'] = datas
    #data
    #print(value['_id'])

#print(data)

#print(jsonify(parent))

# one = collection.find_one({"parent_id":0})

# print(one)

# for info in parent:
    
#     print(info['title'])





#data = {'result': 'this is a test'}
host = ('localhost', 8888)

class Resquest(BaseHTTPRequestHandler):
    
    def do_GET(self):
        path = str(self.path)
       
        parsed_path = urlparse(path)

        path = parsed_path.path
       
        if path == '/change':
            query = parse_qs(parsed_path.query)
            title = query["title"][0]
            url = query["url"][0]
            id = query["id"][0]
            
            client = pymongo.MongoClient("mongodb://localhost:27017/")
            db = client.bookmarks
            collection = db.bookmark

            myquery = { "_id": ObjectId(id) }
            print(ObjectId(id))
            print(title)
            print(url)
            newvalues = { "$set": { "title": title,"href":url } }

            collection.update_one(myquery,newvalues)
            data = {"message":'ok'}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(dumps(data).encode())

            
        else:
            client = pymongo.MongoClient("mongodb://localhost:27017/")
            db = client.bookmarks
            collection = db.bookmark

            parent = collection.find({'parent_id':0})

            data = list(parent)

            for d in data:
                children = collection.find({'parent_id':d['_id']})
                datas = list(children)
                d['children'] = datas

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(dumps(data).encode())

if __name__ == '__main__':
    server = HTTPServer(host, Resquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()

