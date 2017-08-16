import requests
from bs4 import BeautifulSoup

print('\nhello I am working\n')


def spider(max_pages):
    page = 1
    while page <= max_pages:
        url = "https://www.reddit.com/?count=" + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.findAll('a', {'class': "title"}):
            href = link.get('href')
            title = link.string
            print("=======")
            print(title)
            print(href)
            print("======")
        page += 50

def item_info(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    

spider(1000)
print('hello I am working')