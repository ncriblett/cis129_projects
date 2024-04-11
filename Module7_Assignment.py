#Nick Riblett
#Module 7 Assignment
#3/29/24
#This program will turn a dice rolling game into code

from random import *

def main():
    print()
    #initialize variables
    endProgram = 'no'
    playerOne = 'NO NAME'
    playerTwo = 'NO NAME'

    print("This is a two-player dice game. Both players roll one die and the winner is the highest scores")
    #call to inputNames
    playerOne, playerTwo = inputNames(playerOne, playerTwo)

    #while loop to run program again
    while endProgram == 'no':
        #populate variable
        winnersName = 'NO NAME'
        p1Number = 0
        p2Number = 0

        #call to rollDice
        winnersName = rollDice(playerOne, playerTwo)

        #call to displayInfo
        displayInfo(winnersName)

        endProgram = input("Do you want to end the program? (yes/no): ")
    print("Thanks for playing!")

#This function gets the players names
def inputNames(p1Name, p2Name):
    input
    p1Name = input("Player 1, Enter your name: ")
    p2Name = input("Player 2, Enter your name: ")
    return(p1Name, p2Name)

#This function will get the random values
def rollDice(p1Name, p2Name):
    p1Number = randint(1, 6)
    p2Number = randint(1, 6)
    winnerName = "NO NAME"

    print(f"{p1Name} rolled a {p1Number}")
    print(f"{p2Name} rolled a {p2Number}")

    if p1Number == p2Number:
        winnerName = 'TIE'
    elif p1Number > p2Number:
        winnerName = p1Name
    else:
        winnerName = p2Name

    return(winnerName)
    
#This function will display the winner
def displayInfo(winnerName):
    if winnerName != 'TIE':
        print(f"Congradulations {winnerName}, you have won!!")
    elif winnerName == "TIE":
        print("The game ended in a TIE")
    print()
    return


main()
