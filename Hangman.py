import random
from Wordfile import words
import string

def get_valid_word(words):

    word=random.choice(words)      #randomly chooses a word from the list

    while '-' in words or ' ' in words:     #if word consists of '-' or space then choose again
        word = random.choice(words)

    return word.upper()     #to make the letters uppercase

def hangman():

    new_word=get_valid_word(words)
    word_letters=set(new_word)      #set of letters in the word
    alphabet=set(string.ascii_uppercase)
    used_letters=set()      #set of letters that the user has guessed

    lives=10

    while len(word_letters)>0 and lives>0:

        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print(f"\nYou have {lives} lives left and you have used these letters: ", ' '.join(used_letters))

        #what current word is (ie W - R D)
        list1= [letter if letter in used_letters else '-' for letter in new_word]
        print("\nCurrent word:",' '.join(list1))

        #getting user input
        user_letter=input("\nGuess a letter:").upper()

        if user_letter in alphabet-used_letters:    #if letter hasn't been guessed earlier,then add to used_letters
            used_letters.add(user_letter)
            if user_letter in word_letters:         #if letter is in the word, remove it from word_letters
                word_letters.remove(user_letter)

            else:
                lives = lives - 1   # takes away a life if wrong
                print(f"\nYour letter {user_letter} is not in the word.")

        elif user_letter in used_letters:
            print("\nYou have already used letter. Please try another letter.")

        else:       #if user press a special character
            print("\nInvalid letter. Please try again.")

    #comes to this line when len(word_letters) == 0 OR when lives == 0
    if lives==0:
        print(f"\nNo more lives. You lost!\nThe word was {new_word}.")
    else:
        print(f"\nYay! You have guessed the word {new_word} correctly. Congrats!!")

hangman()