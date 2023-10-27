# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 
# Modules

## milestone_2.py
This module contains three functions to: 
1. Generate a list of words
1. Select a word from the list
2. Request the first guess of a letter from the user. The third function is only executed if name = main. 

## milestone_3.py
This module first imports the module milestone_2 so the variable "word" can be used in the game. 

The milestone_3 module contains two functions:
1. **check_guess** converts the user input to lower case and checks whether it is in the word.
1. **request_user_input** contains an infinite loop that requests the user guess a letter until a valid guess is given. Once a valid guess is given, **check_guess** runs as a subfunction.

# Temporary header: Things to add to README as per AiCore project instructions
- Table of Contents, if the file is long.
- A description of the project: what is does, the aim of the project, and what you learned.
- Installation instructions
- Usage instructions
- File structure of the project
- License information
