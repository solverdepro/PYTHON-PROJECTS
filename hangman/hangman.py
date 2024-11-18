import random
import string
from words import words

def get_valid_word():
    valid_word = random.choice(words)
    while "-"in valid_word or " " in valid_word:
        valid_word = random.choice(words)
    return valid_word

def hangman():
    word = get_valid_word()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives  = 6
    while len(word_letters) > 0 and lives > 0:
        print("you have " , lives,"left and " "You have used these letters: ", " ".join(used_letters))

        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("The current word is: ", " ".join(word_list))

        user_letter = input("enter any letter of your choice: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1   
        elif user_letter in used_letters:
            print("you have already use that letter please try again")
        else:
            print("Invalid input please try again!") 
    if lives == 0:
        print("Sorry, you died the word was",word)
    else:
        print("you win, the word was ",word)    




hangman()

    