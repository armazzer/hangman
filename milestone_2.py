
import random

def generate_word():
    word_list = ["strawberry", "rasberry", "mango", "peach", "cherry"]
    print(word_list)
    word = random.choice(word_list)
    print(word)

def request_letter():
    player_guess = input("Please enter a letter of your choice ")
    if len(player_guess) == 1 and player_guess.isalpha() == True:
        print("Good guess!")
    else:
        print("Oops! That is not a valid input")

generate_word()
request_letter()
