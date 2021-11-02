import requests
from bs4 import BeautifulSoup

ascii_steps = [
"""
 +====++
 |    ||
      ||
      ||
      ||
      ||
============
""",
"""
 +====++
 |    ||
 O    ||
      ||
      ||
      ||
============
""",
"""
 +====++
 |    ||
 O    ||
 |    ||
      ||
      ||
============
""",
"""
 +====++
 |    ||
 O    ||
/|    ||
      ||
      ||
============
""",
"""
 +====++
 |    ||
 O    ||
/|\   ||
      ||
      ||
============
""",
"""
 +====++
 |    ||
 O    ||
/|\   ||
/     ||
      ||
============
""",
"""
 +====++
 |    ||
 O    ||
/|\   ||
/ \   ||
      ||
============
"""
]

def get_random_word():
    url = 'https://www.aleatorios.com/'
    document = requests.get(url).text

    html = BeautifulSoup(document, 'html.parser')
    word_element_text = html.find('h1').text
    word = word_element_text.split()[0]

    return word

def get_char_positions(char, word):
    pos = []
    for index, character in enumerate(word):
        if character == char:
            pos.append(index)

    return pos

welcome_msg = '*** Bienvenido al juego del ahorcado. ***\n'
instructions_msg = '\n> Introduce una letra: '

word = get_random_word()
chars = (len(word) * '_ ').split()

atempt = 0

print(welcome_msg)

while True:
    print('   ' + (' '.join(chars)) + '   ')
    letter = input(instructions_msg)

    if letter in word:
        positions = get_char_positions(letter, word)
        for pos in positions:
            chars[pos] = letter
    else:
        print(ascii_steps[atempt])
        atempt += 1

    if atempt == len(ascii_steps):
        print('XXX Perdiste XXX')
        print('La palabra era: ' + word)
        break

    if '_' not in chars:
        print('   ' + (' '.join(chars)) + '   ')
        print('\n+++ GANASTE +++')
