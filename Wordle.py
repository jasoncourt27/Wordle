import random

five_letter_words = [
    "apple", "bread", "crane", "dream", "eagle", "flame", "grape", "heart", "ideal", "joker",
    "knife", "lemon", "mouse", "noble", "ocean", "pearl", "queen", "raven", "salad", "tiger",
    "urban", "vivid", "whale"
]

word = random.choice(five_letter_words)
wordList = list(word)
currentList = []
found = False
turns = 6
currentSolutionList = ['_','_','_','_','_']


while found == False:
    if turns > 0:
        print()
        print("Turns Left:",turns)
        print(currentSolutionList)
        
        validInput = False
        while validInput == False:
            guess = input("Enter your guess (5 letters): ")
            charCount = 0
            for i in guess:
                charCount += 1
            if charCount == 5:
                validInput = True
            else:
                print("Invalid input. Must be 5 letters.")

        guessList = list(guess)
        turns -= 1
        for i in range(len(guessList)):
            for j in range(len(wordList)):
                if guessList[i] == wordList[j]:
                    if i == j:
                        currentSolutionList[i] = guessList[i]
                    else:
                        print()
                        print("'",guessList[i],"'", "is somewhere else in the word")
        
        if currentSolutionList == wordList:
            found = True
            print()
            print("Well done! You found the word:", word)
                       

    else:
        print()
        print("You are out of turns")
        print("The correct word is",word)
        found = True

