import random

word_list = ["strawberry", "rasberry", "mango", "peach", "cherry"]

class Hangman:
    '''This class is used to play the game Hangman.
        Attributes:
            word (str): a random word selected from word_list.
            word_guessed (list): a list of underscores with each underscore representing a character in the word.
            num_letters (int): the number of unique letters in the word.  
            num_lives (int): the number of lives that the player has, defaulting to a start value of 5.
            word_list (list): the list of words from which the attribute 'word' is selected.
            list_of_guesses (list): a list of letters guessed by the player, which is initially empty. 
    '''
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for _ in self.word]
        self.num_letters = len(set([_ for _ in self.word]))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def update_word_guessed(self, guess):
        ''' This function iterates through 'word' and identifies the position of a correctly guessed letter. 'word_guessed' is then updated with the letter, which replaces the underscore at the same index.
        '''
        for char in self.word:
            if char == guess:
                position_char = self.word.index(char)
                self.word_guessed[position_char] = guess

    def check_guess(self, guess):
        '''This function checks whether the guessed letter is in the word. If so, 'update_word_guessed' is called, updating 'word_guessed' with the letter at the appropriate index, and 'num_letters' is reduced by 1. 
        If the letter is not in the word, 'num_lives' is reduced by 1. In either case a relevant message is printed.
        '''
        guess_lower = guess.lower()
        if guess_lower in self.word:
            print(f"Good guess! {guess_lower} is in the word")
            self.update_word_guessed(guess)
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess_lower} is not in the word. Try again")
            print(f"You have {self.num_lives} lives left")
        
    def ask_for_input(self):
        '''This function requests a guess from the player, checks its validty and prints a relevant message. Once a valid guess is given, 'check_guess' is called, and 'list_of_guesses' is updated with the guessed letter. 
        '''
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
