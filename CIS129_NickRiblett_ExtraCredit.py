#Nick Riblett
#4/2/24
#CIS 129
#This code is the extra credit assignment and will play a guessing game with the user

from random import *

def main():
    keepGoing = 'y'
    while keepGoing == 'y':
        counter = GuessNum()
        print(f"Congratulations! You guessed my number in {counter} tries" )
        keepGoing = input("Would you like to play again? (y/n): ")
    print("Thanks for playing!")

#This function will have the user guess the number until they guess correctly
def GuessNum():
   
    userNum = int(input("Guess my number! It's between 1 and 1000. Do it in the fewest guesses: "))
    counter = 1
    randNum = randint(1, 1000)
    
    while userNum != randNum: #checks the user number isn't the same as the random number
        if userNum > randNum: #number too high
            print("Too high. Try again: ")
            userNum = int(input("Guess again: "))
        elif userNum < randNum: #number too low
            print("Too low, Try again: ")
            userNum = int(input("Guess again: "))
        counter = counter + 1 #count to see how many attemps it takes
    
    return(counter)
main()