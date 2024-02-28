#Nick Riblett
#2/27/24
#Lab 4

monthlySales = 0
storeAmount = 0
empAmount = 0
salesIncrease = 0
prompt = 'Enter the montly sales $'

monthlySales = float(input(prompt))

if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else:
    storeAmount = 0

salesIncrease = float(input('Enter percent of slae increase: '))
salesIncrease = salesIncrease / 100

if salesIncrease >= .05:
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
