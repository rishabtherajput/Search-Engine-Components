import requests
from bs4 import BeautifulSoup

def trade(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://nicoblog.org/pc-games/page/'+ str(page)
        source_code = requests.get(url)
        plain_text =  source_code.text
        soup = BeautifulSoup(plain_text,features="html.parser")
        for link in soup.find_all('a',{'rel':'bookmark'}):
            href = link.get('href')
            title = link.string
            #print(href)
            #print(title)
            get_single(href)
        page = page+1


def get_single(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, features="html.parser")
    for item_name in soup.find_all('p'):
        print(item_name.string)



trade(1)