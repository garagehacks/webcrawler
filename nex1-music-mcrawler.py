import requests
from bs4 import BeautifulSoup

def search_spider(max_pages):
    page = 1
    while page < max_pages :
        url = "http://nex1music.ir/pages/"+str(page)+"/?s"
        source_code=requests.get(url)
        make_text = source_code.text
        soup = BeautifulSoup(make_text)
        for link in soup.findAll("a",{"class" : "mre animate"}):
            href =link.get("href")
            print(href)

search_spider(2)



