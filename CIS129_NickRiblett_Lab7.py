#Nick Riblett
#3/29/24
#CIS 129 Lab 7
#This code will show the price of tickets from 3 different sections

SENTINEL = -99

def main():
    #declared variables
    SEATS = [300, 500, 200]
    SECTIONS = ['A', 'B', 'C']
    PRICE = [20, 15, 10]
    keepGoing = 'y'
    grandTotal = 0
    
    while keepGoing == 'y':
        #delcared variables
        ticketsSold = [0,0,0]
        totalPrice = [0,0,0]
        total = 0
        i = 0
        
        #This prints the menu of availible tickets
        print()
        for i in range(3):
            print(f"There are {SEATS[i]} tickets availible at ${PRICE[i]} in section {SECTIONS[i]}")
            i = i + 1

        #This function will get the number of people per section
        for i in range(3):
            ticketsSold[i] = PeoplePerSection(SEATS[i], SECTIONS[i])
            i = i + 1

        #This function will get the total cost
        for i in range (3):
            totalPrice[i] = TotalCost(ticketsSold[i], PRICE[i])
            total = total + totalPrice[i]
            i = i + 1
        grandTotal = grandTotal + total

        #This function will print the total for each section
        for i in range(3):
            PrintValues(ticketsSold[i], SECTIONS[i], PRICE[i], totalPrice[i])
        print(f"The total for all the tickets is ${total}")
        print(f"The grand total for all tickets is {grandTotal}")
    

        keepGoing = str(input("Would you like to make another entry? (y/n): "))

        #This updates the amount of seats left
        for i in range(3):
            SEATS[i] = SEATS[i] - ticketsSold[i]

#This function gets the total number of people for each section and validates them againt the amount of seats in the section
def PeoplePerSection(seats, section):
    ticketsSold = GetValidInput(seats, section)
    if ticketsSold == SENTINEL:
        exit()
    
    return(ticketsSold)

#This function will get the cost for all the tickets in each section
def TotalCost(tickets, price):
    cost = 0
    cost = tickets * price

    return(cost)

#This function validates the user's entery is within our requirments 
def GetValidInput(seatNum, section):
    userNum = (input(f"How many tickets were sold in section {section} (enter {SENTINEL} to quit): "))
    key = 0
    userNum = GetInt(userNum, key)

    while(InvalidInput(userNum, seatNum)):
        userNum = input(f"'{userNum}' is an invalid input please try again: ")
        userNum = GetInt(userNum, key)
        
    return(userNum)

#Returns True if the users number is not in our seat limit
def InvalidInput(userNum, seatNum):
    if userNum == SENTINEL:
        return(False)
    elif userNum > seatNum:
        return(True)
    elif userNum < 0:
        return(True)
    
   #This function ensures we get an integer 
def GetInt(userNum, key):
    if key == 1:
        userNum = input()

    try:
        return int(userNum)
    except ValueError:
        print(f"'{userNum}' is not a valid number. Please try again: ", end = ' ')
        key = 1
        return(GetInt(userNum, key))

#This function will print the cost and toal for all tickets
def PrintValues(seats, section, ticketPrice, totalPrice):
    print(f"{seats} seats in section {section} at ${ticketPrice} is ${totalPrice}")

main()