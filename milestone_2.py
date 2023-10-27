
import random

def generate_word_list():
    word_list = ["strawberry", "rasberry", "mango", "peach", "cherry"]
    # print(word_list)
    return word_list

def select_word():
    word = random.choice(word_list)
    # print(word)
    return word

def request_letter():
    player_guess = input("Please enter a letter of your choice ")
    if len(player_guess) == 1 and player_guess.isalpha() == True:
        print("Good guess!")
    else:
        print("Oops! That is not a valid input")

word_list = generate_word_list()
word = select_word()
if __name__=="__main__":
    letter = request_letter()
