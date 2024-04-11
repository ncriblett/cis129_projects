#Nick Riblett
#3/29/24
#CIS 129 Lab 7
#This code will show the price of tickets from 3 different sections

def main():
    #declared variables
    #Number of seats
    A_SEATS = 300
    B_SEATS = 500
    C_SEATS = 200
    #Price per seat
    seatAcost = 20
    seatBcost = 15
    seatCcost = 10
    keepGoing = 'y'
    total = 0

    while keepGoing == 'y':
        #delcared variables
        sectionA = sectionB = sectionC = costA = costB = costC = 0

        print()
        print(f"Section A has {A_SEATS} tickets availible at ${seatAcost} each \nSection B has {B_SEATS} tickets availible at ${seatBcost} each\nSection C has {C_SEATS} tickets availible at ${seatCcost} each")

        #This function will get the number of people per section
        sectionA, sectionB, sectionC = peoplePerSection(A_SEATS, B_SEATS, C_SEATS)


        #This function will get the total cost
        costA, costB, costC = totalCost(sectionA, sectionB, sectionC,seatAcost, seatBcost, seatCcost)

        #This function will display the total
        total = showTotal(sectionA, sectionB, sectionC, costA, costB, costC, seatAcost, seatBcost, seatCcost, total)
        A_SEATS = A_SEATS - sectionA
        B_SEATS = B_SEATS - sectionB
        C_SEATS = C_SEATS - sectionC

        keepGoing = str(input("Would you like to make another entry? (y/n): "))

#THis function gets the total number of people for each section and validates them againt the amount of seats in the section
def peoplePerSection(A_SEATS, B_SEATS, C_SEATS):

    sectionA = int(input("How many tickets in section A were sold?: "))
    while sectionA > A_SEATS and sectionA > 0:
        print("We do not have that many seats, please try again.")
        sectionA = int(input("How many tickets in section A were sold?: "))
    
    sectionB = int(input("How many tickets in section B were sold?: "))
    while sectionB > B_SEATS and sectionB > 0:
        print("We do not have that many seats, please try again.")
        sectionB = int(input("How many tickets in section B were sold?: "))

    sectionC = int(input("How many tickets in section C were sold?: ")) 
    while sectionC > C_SEATS and sectionC > 0:
        print("We do not have that many seats, please try again.")
        sectionC = int(input("How many tickets in section C were sold?: "))
    
    return(sectionA, sectionB, sectionC)

#This function will get the cost for all the tickets in each section
def totalCost(sectionA, sectionB, sectionC,A_cost, B_cost, C_cost):

    costA = sectionA * A_cost
    costB = sectionB * B_cost
    costC = sectionC * C_cost

    return(costA, costB, costC)

#This function prints the total for all the tickts
def showTotal(A, B, C, costA, costB, costC, acost, bcost, ccost, grandTotal):
    total = 0
    total = costA + costB + costC
    grandTotal = grandTotal + total

    print(f'{A} tickets in section A at ${acost} each is ${costA}' if A > 1 or A == 0 else f'{A} ticket in section A is ${costA}')
    print(f'{B} tickets in section B at ${bcost} each is ${costB}' if B > 1 or B == 0 else f'{B} ticket in section B is ${costB}')
    print(f'{C} tickets in section C at ${ccost} each is ${costC}' if C > 1 or C == 0 else f'{C} ticket in section C is ${costC}')
    print() 
    print(f' ${costA:> 2}\n ${costB:> 2}\n+${costC:> 1}')
    print('--------')
    print(f" ${total:> 2}")
    print()
    print("The total for this ticket entry is $", total)
    print("The grand total for all the tickets is $", grandTotal)
    return(grandTotal)

main()