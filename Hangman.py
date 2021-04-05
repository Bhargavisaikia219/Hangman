import random
from Wordfile import words
import string

def get_valid_word(words):
    word=random.choice(words)
    while '-' in words or ' ' in words:
        word = random.choice(words)
    return word.upper()

def hangman():

    new_word=get_valid_word(words)
    word_letters=set(new_word)
    alphabet=set(string.ascii_uppercase)
    used_letters=set()

    while len(word_letters)>0:
        print("You have guessed these letters:", ' '.join(used_letters))
        list1= [letter if letter in used_letters else '-' for letter in new_word]
        print("Current word:",' '.join(list1))

        user_letter=input("Guess a letter:").upper()

        if user_letter in alphabet-used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print("You have already used letter. Please try again.")
        else:
            print("Invalid character. Please try again.")

hangman()