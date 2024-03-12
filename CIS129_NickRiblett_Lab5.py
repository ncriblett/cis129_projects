#Nick Riblett
#CIS 129 Lab 5 3/14/24
# This code gets the total number of bottles for a week and calculates the total earned from the bottles

#Declared variables
NBR_OF_DAY= 7
keepGoing = 'y'
PAYOUT_PER_BOTTLE = 0.10

while keepGoing == 'y':
    counter = 1 #Declares variables
    totalBottles = 0 
    todayBottles = 0
    totalPayout = 0
    while counter <= NBR_OF_DAY: #Gets data for 7 days
        todayBottles = int(input(f'Enter number of bottles for day #{counter}: '))
        totalBottles = totalBottles + todayBottles
        counter += 1
   
    totalPayout = totalBottles * PAYOUT_PER_BOTTLE #gets total payout at 10 cents a bottle

    print()
    print("The total number of bottles collected is ", totalBottles)
    print(f"The total paid out is ${totalPayout:.2f}")
    print()

    print("Do you want to enter another week's worth of data?")
    keepGoing = input("(Enter y or n): ")
    print()

          
