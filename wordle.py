'''
Word guessing game 
This program will execute a word guessing game where the user has to guess a random word within a limited number of attempts.This program will later give a color depending on the letter position that you typed. correct letters in the correct Position (green),correct letters in the wrong position (yellow), and incorrect letters (red).
Features:
Level selection: Let the user to select a game level (from 5-8 letters)
Guess attempts: Provides the user a set number of attempts to guess the word
File-Based Word Pool: get random words from specific files for the game.
Game loop:
Get user input to guess the word for the game
Provides feedback on user’s guess by showing the guessed word with colors
Exits the game if the user guess is correct
Main Function: Controls the flow for the game by coordinating other operations.
Input handling: Manages level selection and guessing user input.
Checking the word: Check the correctness of the guess word and compare with the chosen words and give a feedback
Operations on Files: Retrieves words from designated level files to supply the game with a reservoir of terms.
Display functions: Prints the guessed word with color-coded characters.
'''
import random
import sys
import os
win= 1
# ANSI color codes for terminal text color
COLORS = {
    "RESET": "\u001b[0m",
    "GREEN": "\u001b[32m",
    "YELLOW": "\u001b[33m",
    "RED": "\u001b[31m"
}

# Status Constants
EXACT = 2
CLOSE = 1
WRONG = 0

def main():
    # get a level and initialize guess attempts
    level = level_input()
    guesses = level + 1
    
    # get a random word based on the chosen level
    choice = read_file(level)
    status = [0] * len(choice)  # Initialize status for each character
    
    print(f"You have {guesses} tries to guess the {level}-letter word I'm thinking of")
    
    for i in range(guesses):
        # Obtain guess from user
        guess = guess_input(choice, i + 1)
        
        # Check the guess against the chosen word and update status
        score = checking(choice, guess, status)
        
        # Print the guessed word with appropriate color coding
        print_word(guess, len(guess), status)
        
        # Check if the guess is entirely correct and exit if so
        if score == EXACT * len(guess):
            store_score()
            sys.exit()
    
    print(choice)  # Print the correct word if the user couldn't guess it

def checking(choice, guess, status):
    score = 0
    # Check each character of the guess against the chosen word
    for i, char in enumerate(choice):
        if guess[i] == char:
            score += EXACT
            status[i] = EXACT  # Mark correct position
        elif guess[i] in choice:
            score += CLOSE
            status[i] = CLOSE  # Mark correct character, wrong position
        else:
            score += WRONG
            status[i] = WRONG  # Mark incorrect character
    return score

def guess_input(choice, tries):
    # Prompt the user for a guess
    while True:
        x = input(f"Guess {tries}: ")
        if len(x) == len(choice):
            return x

def read_file(x):
    try:
        # Read a random word from a file based according to the level
        file_path = f"{x}.txt"
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if lines:  # Check if the file is not empty
                random_line = random.choice(lines).strip()
                return random_line
            else:
                return "File is empty"
    except FileNotFoundError:
        return f"File '{x}.txt' not found"
    except IOError:
        return "Error reading the file"

def level_input():
    # Prompt the user to choose a level between 1 and 4
    while True:
        try: #checking if the user input the wrong data
            level = int(input("enter the level from 1 to 4 : "))
            # Check if the input is between 1 and 4
            if 0 < level < 5:
                return level + 4
            else:
                print("The level must be 1, 2, 3, or 4")
        except ValueError:
            print("Invalid input. The level must be 1, 2, 3, or 4")
            
def print_word(guess, wordsize, status):
    # Print the guessed word character-by-character with colors
    for i in range(wordsize):
        if status[i] == EXACT:
            print(COLORS["GREEN"] + guess[i] + COLORS["RESET"], end="")
        elif status[i] == CLOSE:
            print(COLORS["YELLOW"] + guess[i] + COLORS["RESET"], end="")
        elif status[i] == WRONG:
            print(COLORS["RED"] + guess[i] + COLORS["RESET"], end="")
    print()
def store_score():
    reader=0
    if os.path.exists("cps109_a1_output.txt"):
        with open("cps109_a1_output.txt",'r') as file:
            reader =int(file.read())
            
    try:
        with open('cps109_a1_output.txt', "w") as file:
            file.write(str(reader+1))
    except IOError:
        print("Error adding task to the file.")


if __name__ == "__main__":
    main()
    
