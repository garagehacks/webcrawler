import requests
from bs4 import BeautifulSoup

def search_spider(max_pages):
    page = 1
    while page < max_pages :
        url = "http://pop-music.ir/?blogs=" + str(page) + "%2C5&s=%D9%81%D8%B1%D8%B2%D8%A7%D8%AF+%D9%81%D8%B1%D8%B2%DB%8C%D9%86"
        source_code=requests.get(url)
        make_text = source_code.text
        soup = BeautifulSoup(make_text)
        for link in soup.findAll("a",{"rel" : "bookmark"}):
            href =link.get("href")
            title =link.get("title")
            print(href)
            print(title)



search_spider(2)


