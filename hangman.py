import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabe  - used_letters:
        used_letters.add(user_letter)
        if used_letter in word_letters:
            word_letters.remove(user_input)


user_input = input('Type something: ')