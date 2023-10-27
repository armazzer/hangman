import milestone_2

def check_guess(guess):
    guess_lower = guess.lower()
    if guess_lower in milestone_2.word:
        print(f"Good guess! {guess_lower} is in the word")
    else:
        print(f"Sorry, {guess_lower} is not in the word. Try again")

def ask_for_input():
    while True:
        guess = input("Please enter a letter of your choice ")
        if len(guess) == 1 and guess.isalpha() == True:
            break    
        else:
            print("Invalid letter. Please enter a single alphabetical character")

    check_guess(guess)

ask_for_input()

