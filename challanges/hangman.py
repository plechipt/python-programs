import requests
from bs4 import BeautifulSoup
import random

# scraping words from site
url = requests.get('https://www.manythings.org/vocabulary/lists/l/words.php?f=noll11')
bs = BeautifulSoup(url.content, 'html.parser')
words = bs.find_all('li')

# hangman part
def random_word():
    return words[random.randint(0, len(words))].get_text() # random word from words
word_letters = [letter for letter in word]

def is_correct()
    


'''
user_input = input('Enter a letter: ')
