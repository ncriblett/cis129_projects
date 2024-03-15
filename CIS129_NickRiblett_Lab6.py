# Nick Riblett
# 3/26/24
# Lab 6
# This code will be able to calculate the number of hotdogs and buns needed for a cook out. 
#It will also give the amount left over. This was given to us from pseudocode
from math import *

def main():
    total = 0

    total = getTotalHotdogs()

    DOGS = 10
    BUNS = 8

    dogsLeft = 0
    bunsLeft = 0
    minDogs = 0
    minBuns = 0

    dogsLeft = (DOGS - total % DOGS) % DOGS
    minDogs =  ceil(total / DOGS)
    bunsLeft = (BUNS - total % BUNS) % BUNS
    minBuns = ceil(total / BUNS)
    ShowResults(dogsLeft, minDogs, bunsLeft, minBuns)

def getTotalHotdogs():
    numPeople = 0
    hotdogs = 0

    numPeople = int(input("Enter the total number of people attending the cookout: "))
    hotdogs = int(input("Enter the number of hotdogs for each person: "))

    total = numPeople * hotdogs
    return(total)

def ShowResults(dogsLeft, minDogs, bunsLeft, minBuns):
    print("Minimum packages of hot dogs needed: ", minDogs)
    print("Minimum packages of hot dog buns needed: ", minBuns)
    print("Hot dogs left over: ", dogsLeft)
    print("Hot dog buns left over: ", bunsLeft)



