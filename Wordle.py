import random
import re

GREEN = '\033[92m'
YELLOW = '\033[93m'
GREY = '\033[90m'
RESET = '\033[0m'

five_letter_words = [
    "apple", "bread", "crane", "dream", "eagle", "flame", "grape", "heart", "ideal", "joker",
    "knife", "lemon", "mouse", "noble", "ocean", "pearl", "queen", "raven", "salad", "tiger",
    "urban", "vivid", "whale"
]

def choose_word():
    return random.choice(five_letter_words)

def validate_guess(guess):
    return len(guess) == 5 and re.match("^[a-zA-Z]{5}$", guess)

def get_feedback(guess, word):
    feedback = ""
    word_dict = {}
    
    for i, letter in enumerate(word):
        word_dict[letter] = word_dict.get(letter, 0) + 1

    for i, letter in enumerate(guess):
        if letter == word[i]:
            feedback += GREEN + letter + RESET
            word_dict[letter] -= 1
        elif letter in word and word_dict[letter] > 0:
            feedback += YELLOW + letter + RESET
            word_dict[letter] -= 1
        else:
            feedback += GREY + letter + RESET

    return feedback

def play_game():
    word = choose_word()
    turns = 6
    print("Welcome to Wordle!\n")

    while turns > 0:
        print(f"Turns Left: {turns}")

        guess = input("Enter your guess (5 letters): ").lower()
        while not validate_guess(guess):
            print("Invalid input. Make sure it's a 5-letter word.")
            guess = input("Enter your guess (5 letters): ").lower()

        feedback = get_feedback(guess, word)
        print("Feedback: ", feedback)
        print()
        if guess == word:
            print(f"Well done! You found the word: {word}")
            return

        turns -= 1

    print(f"You are out of turns. The correct word was: {word}")

play_game()
