#Nick Riblett
# My 3rd Python Lab in CIS129
#Coffee shop menu

COFFEECOST = 5
MUFFINCOST = 4
coffeeSubTotal = 0.0
muffinSubTotal = 0.0
TAX = .06
totalTax = 0.0
subTotal = 0.0
grandTotal = 0.0



print("My Coffee and Muffin shop")
userCoffee = int(input("How many coffees would you like?\n")) #Gets number of coffees from user
userMuffin = int(input("How many muffins would you like?\n")) #Gets number of muffins from user

coffeeSubTotal = userCoffee * COFFEECOST #Total cost of coffee
muffinSubTotal = userMuffin * MUFFINCOST #Total cost of muffin

subTotal = (coffeeSubTotal) + (muffinSubTotal) #Total of coffee + muffins
totalTax = subTotal * TAX #Cost of tax
grandTotal = totalTax + subTotal # cost of coffee + muffins + tax

print("My Coffee and Muffin shop")
print(userCoffee,"Coffee at $5 each: $",coffeeSubTotal)
print(userMuffin,"Muffin at $4 each: $",muffinSubTotal)
print("6% tax: $", totalTax)
print("Total: $", grandTotal)




