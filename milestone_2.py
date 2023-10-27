import random
word_list = ["strawberry", "rasberry", "mango", "peach", "cherry"]
print(word_list)
word = random.choice(word_list)
print(word)
guess = input("Please enter a letter of your choice ")
if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess!")
else:
    print("Oops! That is not a valid input")