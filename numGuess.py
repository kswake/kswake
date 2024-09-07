# simple number guessing game
import os
import random

# instantiate upper and lower bounds as zero
rangeLB = 0
rangeUB = 0
numGuesses = 0
currentGuess = 0
validRange = False 

print("Welcome!")

#get lower and upper bounds and validate that they are integers in ascending order:
while validRange == False:

    try:
        rangeLB = int(input("Enter lower bound: "))
        rangeUB = int(input("Enter upper bound: "))
        if rangeLB < rangeUB:
            validRange = True
        else:
            print("Make sure your integers are in ascending order!")
    except ValueError:
        print("Make sure you only enter integers!")   

#generate random number within the user-input bounds
target = random.randrange(rangeLB,rangeUB)

# make user guess until they get it, tracking num of guesses
while currentGuess != target:
    
    print("You've guessed " + str(numGuesses) + " times so far.")
    
    try:
        currentGuess = int(input("Guess a number between " + str(rangeLB) + " and " + str(rangeUB) +": "))
        
        if target > currentGuess: 
            print("Too low!")
        elif target < currentGuess:
            print("Too high!")         
        
        numGuesses += 1    

    except ValueError:
        print("Your guess must be an integer!")

print("Congrats, you correctly guessed "+str(target)+" in only "+str(numGuesses)+" guesses!")