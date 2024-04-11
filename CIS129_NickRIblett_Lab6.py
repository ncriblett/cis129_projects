# Nick Riblett
# 3/20/24
# Lab 6
# This lab will get the amount of hot dogs and buns needed for a cookout. It will also give the left overs

from math import *

def main():
    DOGS = 10 #Constants 
    BUNS = 8

    total = getTotalHotDogs()

    dogsLeft = 0 #declared variables
    bunsLeft = 0
    minDogs = 0
    minBuns = 0

    dogsLeft = (DOGS - total % DOGS) % DOGS #calculates the hot dogs left
    minDogs = ceil(total/DOGS) #minimum number of hot dog packages
    bunsLeft = (BUNS - total % BUNS) % BUNS # calculates the left over buns
    minBuns = ceil(total / BUNS) # minimum number of bun packages needed

    showResults(dogsLeft, minDogs, bunsLeft, minBuns)

def getTotalHotDogs(): # gets the number of people at the cookout and the a ount of hotdogs needed
    people = 0
    hotDogs = 0

    people = int(input("Enter the number of people attending the cookout: "))
    hotDogs = int(input("Enter the number of hot dogs for each person: "))

    total = people * hotDogs
    return(total)

def showResults(dogsLeft, minDogs, bunsLeft, minBuns): # Shows the results for the cookout
    print("Minimum packages of hot dogs needed: ", minDogs)
    print("Minimum packages of hot dog buns needed: ", minBuns)
    print("Hot dogs left over: ", dogsLeft)
    print("Hot dog buns left over: ", bunsLeft)

    return
main()