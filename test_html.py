from bs4 import BeautifulSoup

file = open(r'bookmarks.html','r',encoding='utf-8')

#file=open(r'bookmarks.html') #打开html
Soup = BeautifulSoup(file.read(), 'lxml') #file本身是一个HTTPResponse类型的对象，通过调用它的read属性返回网页内容
title=Soup.select('TITLE') #定位标题
title = Soup.title
#context=Soup.select('#container .wrapper p') #定位主体内容
print(title.text)

parent_infos = Soup.select('DT H3')

#child = Soup.select('DL DT A')

# for info in  child:
#     print(info.text)
#print(parent)

for parent_info in parent_infos:
    if parent_info.parent.nextSibling:
        child_infos = parent_info.parent.nextSibling.select('A')
        print(parent_info.text)
        for child_info in child_infos:
            print(child_info.text)
            print(child_info['href'])
        
    



