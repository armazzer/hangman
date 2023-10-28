import random

word_list = ["strawberry", "rasberry", "mango", "peach", "cherry"]

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for _ in self.word]
        self.num_letters = len(set([_ for _ in self.word]))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess_lower = guess.lower()
        if guess_lower in self.word:
            print(f"Good guess! {guess_lower} is in the word")
            for char in self.word:
                if char == guess:
                    position_char = self.word.index(char)
                    self.word_guessed[position_char] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess_lower} is not in the word. Try again")
            print(f"You have {self.num_lives} lives left")
        
    def ask_for_input(self):
        while True:
            guess = input("Please enter a letter of your choice ")
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please enter a single alphabetical character")  
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                

test_a = Hangman(word_list)
test_a.ask_for_input()
