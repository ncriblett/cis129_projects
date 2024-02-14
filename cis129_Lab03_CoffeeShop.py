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



print("My Coffee and Muffin shop")
userCoffee = int(input("How many coffees would you like?\n")) #Gets number of coffees from user
userMuffin = int(input("How many muffins would you like?\n")) #Gets number of muffins from user
userDoughnut = int(input("How many doughnuts would you like?\n")) #Gets number of doughnuts from user
userBagel = int(input("How many bagels would you like?\n")) #Gets number of bagels from user

coffeeSubTotal = userCoffee * COFFEECOST #Total cost of coffee
muffinSubTotal = userMuffin * MUFFINCOST #Total cost of muffin
doughnutSubTotal = userDoughnut * DOUGHNUTCOST #Total cost of doughnuts
bagelSubTotal = userBagel * BAGELCOST #Total cost of bagels


subTotal = (coffeeSubTotal) + (muffinSubTotal) + doughnutSubTotal + bagelSubTotal #Total of coffee + muffins + doughnuts + bagel
totalTax = subTotal * TAX #Cost of tax
grandTotal = totalTax + subTotal # cost of coffee + muffins + tax

print("My Coffee and Muffin shop")
print(userCoffee,"Coffee at $5 each: $",coffeeSubTotal)
print(userMuffin,"Muffin at $4 each: $",muffinSubTotal)
print(userBagel, "Bagels at $2 easch: $", bagelSubTotal)
print(userDoughnut, "Doughnuts at $3 each: $", doughnutSubTotal)
print("6% tax: $", totalTax)
print("Total: $", grandTotal)



