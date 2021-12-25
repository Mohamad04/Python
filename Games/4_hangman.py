

#4 Question    Hangman

import random
from listOfWords import words
import string



def get_valid_word(words):
    word = random.choice(words)     #randomly chooses something from the list

    while '-' in words or ' ' in word:
        word = random.choice(words)
    
    return word.upper()





def hangman():
    word = get_valid_word(words)  
    word_letters = set(word)              # letters in the word
    alphabet = set(string.ascii_uppercase)# predetermined list of uppers case chars
    used_letters = set()                  # what the user has guessed

    # getting user input
    while len(word_letters) > 0:
        # letters used
        # ' '.join(['a', 'b', 'c'])  --->  'a b c'
        print("You have used these letters: ", ' '.join(used_letters))

        # what current word is (ie  W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))


        user_input = input("Guess a letter: ").upper()

        if user_input in alphabet - used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
        
        elif user_input in used_letters:
            print("you have already used that character. try again")

        else:
            print("invalid character  !")
    
    # gets here when len(word_letters) == 0 




hangman()