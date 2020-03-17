import pymongo
from bs4 import BeautifulSoup

file = open(r'bookmarks.html','r',encoding='utf-8')



#file=open(r'bookmarks.html') #打开html
Soup = BeautifulSoup(file.read(), 'lxml') #file本身是一个HTTPResponse类型的对象，通过调用它的read属性返回网页内容
title=Soup.select('TITLE') #定位标题
title = Soup.title

parent_infos = Soup.select('DT H3')

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.bookmarks
collection = db.bookmark

for parent_info in parent_infos:
    if parent_info.text != "收藏栏":
        if parent_info.parent.nextSibling:
            child_infos = parent_info.parent.nextSibling.select('A')
            data = {
                "title":parent_info.text,
                "href":"",
                "icon":'https://www.80shihua.com/favicon.ico',
                "desc":parent_info.text,
                "parent_id" :0
            }
            inserted_id = collection.insert_one(data).inserted_id
            print(inserted_id)
            for child_info in child_infos:
                data = {
                    "title":child_info.text,
                    "href":child_info['href'],
                    "icon":'https://www.80shihua.com/favicon.ico',
                    "desc":child_info.text,
                    "parent_id" :inserted_id
                }
                collection.insert_one(data)
                #print(child_info.text)
                #print(child_info['href'])