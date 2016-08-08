import requests
from bs4 import BeautifulSoup


def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code)
    site_attribute = r"module--track__heading heading--sm"
    for post_text in soup.findAll('h5', {'class': site_attribute}):
        content = post_text.string
        words = content.lower().split()
        for each_word in words:
            print(each_word)
            word_list.append(each_word)
    word_cleanup(word_list)


def word_cleanup(trash):
    clean_word_list = []
    for clean_word in trash:
        symbols = "!£$%^*&()_+=-`¬|,.<>/?;:'@.#~[{]}\""
        for i in range(0, len(symbols)):
            clean_word = clean_word.replace(symbols[i], "")
        if len(clean_word) > 0:
            print(clean_word)
            clean_word_list.append(clean_word_list)


start("https://cgcookie.com/courses")
