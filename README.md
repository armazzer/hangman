# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 
# Modules

## milestone_2.py

### Learning objectives
The objective of this milestone was generate the basic elements of the hangman game using basic python code. This constituted defining some small functions to generate the game variables. 

### Module code summary
This module contains three functions: 
1. **generate_word_list** generates a list of words, *word_list*.
1. **select_word** selects a *word* from word_list.
2. **request_letter** requests the first guess of a letter from the user. This function is only executed if name = main. 

## milestone_3.py

### Learning objectives
This module aimed to develop further building blocks for the game in slightly more complex functions.  

### Module code summary
This module first imports the module milestone_2 so the variable *word* can be used in the game. 

The milestone_3 module contains two functions:
1. **check_guess** converts the user input to lower case and checks whether it is in the *word*.
1. **request_user_input** contains an infinite loop that requests the user guess a letter until a valid guess is given. Once a valid guess is given, **check_guess** runs as a subfunction.

## milestone_4.py

### Learning objectives
The aim in this module was to re-factor the hangman game using an OOP approach. A new class was defined to contain the game, and the building blocks (functions) developed in milestone_2 and milestone_3 were utilised and built on within the class (as methods).   

### Module code summary
The class Hangman created with a constructor containing the following attributes:
- self.word = a random word selected from the *word_list*.
- self.word_guessed = a list of underscores with each underscore representing a character in *word*.
- self.num_letters = the number of unique letters in *word*.  
- self.num_lives = the number of lives that the player has, defaulting to a start value of 5.
- self.word_list = the *word_list*
- self.list_of_guesses = a list of letters guessed, which is initially empty.

Two methods are defined within the class:
1. **check_guess** checks whether the guessed letter is in the word. If so, word_guessed is updated with the letter at the appropriate index, and *num_letters* is reduced by 1. 
If the letter is not in the word, *num_lives* is reduced by 1. In either case a relevant message is printed.
1. **ask_for_input** requests a guess from the player, checks it's validty and prints a relevant message. Once a valid guess is given, **check_guess** runs as a subfunction, and *list_of_guesses* is updated with the guessed letter. 

# Temporary header: Things to add to README as per AiCore project instructions
- Table of Contents, if the file is long.
- A description of the project: what is does, the aim of the project, and what you learned.
- Installation instructions
- Usage instructions
- File structure of the project
- License information
