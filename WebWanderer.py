'''
import requests
from bs4 import BeautifulSoup

def web_wanderer(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://buckysroom.org/trade/search.php?page=' + str(page)
        source_code = requests.get(url)                                         #where data's stored
        plain = source_code.text                                                #makes plaintext for bs
        soup = BeautifulSoup(plain)                                             #lets bs parse text
        for link in soup.findAll('a', {'class' : 'item-name'}):                 #gives bs specific object (a = anchor)
            href = "http://buckysroom.org" + link.get('href')                   #assigns link to href
            title = link.string                                                 #assigns string to title
            print(href)
            print(title)

web_wanderer(1)

'''