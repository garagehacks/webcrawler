import requests
from bs4 import BeautifulSoup

def search_spider():
        qamus=open("hashem.txt","w")

        url = "http://nex1music.ir/%D8%AF%D8%A7%D9%86%D9%84%D9%88%D8%AF-%D8%A2%D9%87%D9%86%DA%AF-%D9%85%D9%87%D8%B1%D8%AF%D8%A7%D8%AF-%D8%A7%DB%8C%DA%A9%D8%B3-%D8%AA%D9%88-%D9%88-%D9%85%D8%B3%D8%B9%D9%88%D8%AF-%D8%A7%DA%86-%D9%BE%DB%8C/"
        source_code=requests.get(url)
        make_text = source_code.text
        soup = BeautifulSoup(make_text)

        for link in soup.findAll('a', href=True , text="دانلود آهنگ با کیفیت 320"):
            qamus.write(link['href'])
            print( link['href'])



search_spider()


