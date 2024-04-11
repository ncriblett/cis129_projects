#Nick Riblett
# My 3rd Python Lab in CIS129
#Coffee shop menu

COFFEECOST = 5              #All variables and constants used
MUFFINCOST = 4
DOUGHNUTCOST = 3
BAGELCOST = 2
coffeeSubTotal = 0.0
muffinSubTotal = 0.0
doughnutSubTotal = 0.0
bagelSubTotal = 0.0
TAX = .06
totalTax = 0.0
subTotal = 0.0
grandTotal = 0.0



print('*************************************')
print("My Coffee and Muffin shop")
userCoffee = int(input("How many coffees would you like?\n")) #Gets number of coffees from user
userMuffin = int(input("How many muffins would you like?\n")) #Gets number of muffins from user
userDoughnut = int(input("How many doughnuts would you like?\n")) #Gets number of doughnuts from user
userBagel = int(input("How many bagels would you like?\n")) #Gets number of bagels from user
print('*************************************')

coffeeSubTotal = userCoffee * COFFEECOST #Total cost of coffee
muffinSubTotal = userMuffin * MUFFINCOST #Total cost of muffin
doughnutSubTotal = userDoughnut * DOUGHNUTCOST #Total cost of doughnuts
bagelSubTotal = userBagel * BAGELCOST #Total cost of bagels


subTotal = (coffeeSubTotal) + (muffinSubTotal) + doughnutSubTotal + bagelSubTotal #Total of coffee + muffins + doughnuts + bagel
totalTax = subTotal * TAX #Cost of tax
grandTotal = totalTax + subTotal # cost of coffee + muffins + tax

print('*************************************')
print("My Coffee and Muffin Shop Receipt")
if userCoffee == 1:
    print(userCoffee,"Coffee at $5 each: $",coffeeSubTotal)
else:
    print(userCoffee,"Coffees at $5 each: $",coffeeSubTotal)
if userMuffin == 1:
    print(userMuffin,"Muffin at $4 each: $",muffinSubTotal)
else:
    print(userMuffin,"Muffins at $4 each: $",muffinSubTotal)
if userDoughnut == 1:
    print(userDoughnut, "Doughnut at $3 each: $", doughnutSubTotal)
else:
    print(userDoughnut, "Doughnuts at $3 each: $", doughnutSubTotal)
if userBagel == 1:
    print(userBagel, "Bagel at $2 each: $", bagelSubTotal)
else:
    print(userBagel, "Bagels at $2 each: $", bagelSubTotal)

print("6% tax: $", f'{totalTax:.2f}')
print('--------')
print("Total: $", f'{grandTotal:.2f}')
print('*************************************')
print("Thank you for comming! Have a great day!")




