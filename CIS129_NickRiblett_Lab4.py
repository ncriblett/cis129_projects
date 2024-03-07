#Nick Riblett
#2/27/24
#Lab 4

#Declared variables
monthlySales = 0
storeAmount = 0
empAmount = 0
salesIncrease = 0
prompt = 'Enter the montly sales $'

monthlySales = float(input(prompt)) #This gets the monthly sales

if monthlySales >= 110000: #This calculates the store bonus based on the monthly sales
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else:
    storeAmount = 0

salesIncrease = float(input('Enter percent of slae increase: ')) #Gets the increase of sales in a percent
salesIncrease = salesIncrease / 100 #Turns percent sales into a decimal

if salesIncrease >= .05: #This gets the bonus given to every employees 
    empAmount = 75
elif salesIncrease >= .04:
    empAmount = 50
elif salesIncrease >= .03:
    empAmount = 40
else:
    empAmount = 0

print("The store bonus amount is $", storeAmount)
print("THe bonus amount is $", empAmount)
if (storeAmount == 6000) and (empAmount == 75): 
    print('Congrats! You have reached the highest bonus amounts possible!')
