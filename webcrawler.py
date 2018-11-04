import requests
from bs4 import BeautifulSoup

def trade(max_pages):
    page = 1
    f = open('web.txt', 'w')
    while page <= max_pages:
        url = 'https://nicoblog.org/pc-games/page/'+ str(page)
        source_code = requests.get(url)
        plain_text =  source_code.text
        soup = BeautifulSoup(plain_text,features="html.parser")
        for link in soup.find_all('a'):
            href = link.get('href')
            title = link.string
            print(href)
            print(title)
            f.write(href+'\n')
            f.write(str(title))
        page = page+1

    f.close()
trade(4)



