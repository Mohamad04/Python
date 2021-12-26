

#4 Question    Hangman

import random
from listOfWords import words
import string



def get_valid_word(words):
    word = random.choice(words)     #randomly chooses something from the list
    
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()





def hangman():
    word = get_valid_word(words)  
    word_letters = set(word)              # letters in the word
    alphabet = set(string.ascii_uppercase)# predetermined list of uppers case chars
    used_letters = set()                  # what the user has guessed

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        if len(used_letters) > 0:
            print("You have ", lives, " lives left and you have used these letters: ", ' '.join(used_letters))

        # what current word is (ie  W - R--D--)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))


        user_input = input("Guess a letter: ").upper()

        if user_input in alphabet - used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
            
            else:
                lives -=1       # takes away a life if wrong 
                print("Letter is not in word!")
        
        elif user_input in used_letters:
            print("you have already used that character. try again")

        else:
            print("invalid character  !")
    
    # gets here when len(word_letters) == 0  or when lives == 0  

    if lives == 0:
        print("You died, Sorry the word was ", word)
    
    else:
        print("Congrats you found it  ", word, " !!")





hangman()