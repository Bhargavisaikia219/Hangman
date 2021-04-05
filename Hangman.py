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
    lives=10

    while len(word_letters)>0 and lives>0:
        print("\nYou have guessed these letters:", ' '.join(used_letters))
        list1= [letter if letter in used_letters else '-' for letter in new_word]
        print("\nCurrent word:",' '.join(list1))

        user_letter=input("\nGuess a letter:").upper()

        if user_letter in alphabet-used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print(f"\nYour letter {user_letter} is not in the word.")
                print(f"\nlives left:{lives}")

        elif user_letter in used_letters:
            print("\nYou have already used letter. Please try another letter.")
        else:
            print("\nInvalid letter. Please try again.")

    if lives==0:
        print(f"\nNo more lives. You lost!\nThe word was {new_word}.")
    else:
        print(f"\nYay! You have guessed the word {new_word} correctly. Congrats!!")

hangman()