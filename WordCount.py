import requests
from bs4 import BeautifulSoup
import operator


def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code)
    site_attribute = r"module--track__heading heading--sm"
    for post_text in soup.findAll('h5', {'class': site_attribute}):
        content = post_text.string
        words = content.lower().split()
        for each_word in words:
            word_list.append(each_word)
    word_cleanup(word_list)


def word_cleanup(unsorted):
    clean_word_list = []
    for clean_word in unsorted:
        symbols = "!£$%^*&()_+=-`¬|,.<>/?;:'@.#~[{]}\""
        for i in range(0, len(symbols)):
            clean_word = clean_word.replace(symbols[i], "")
        if len(clean_word) > 0:
            clean_word_list.append(clean_word)
    dictionary_count(clean_word_list)

# used clean_word_list, got [...]
# means product repeats within self


def dictionary_count(clean_list):
    dictionary = {}
    for clean_words in clean_list:
        if clean_words in dictionary:
            dictionary[clean_words] += 1
        else:
            dictionary[clean_words] = 1
    for key, value in sorted(dictionary.items(), key=operator.itemgetter(1)):
        print(key, value)

start("https://cgcookie.com/courses")
