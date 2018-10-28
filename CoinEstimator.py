# This Program will calculate how much money you have using the weight of each type of coin.
# In addition it will inform you how many coin wrappers you will need of each type, and how many coins of each type.

print("Start CoinEstimator!")
print("Find out how much your change is worth without counting it all.")

# Asks the user for their desired units of weight(grams or pounds).
units = ''
while units != 'G' and units != 'P':
    units = input("Input your desired weight units.  Enter 'G' for grams or 'P' for pounds")
    if units != 'G' and units != 'P':
        print("You entered an invalid value.  Try Again.")

# Asks the user for the weight of each coin
print("Please enter the weight of each of your types of coins.  If you don't have any of a certain type, Enter '0'.")
pennies_weight = float(input("Please enter the weight of your pennies: "))
nickels_weight = float(input("Please enter the weight of your nickels: "))
dimes_weight = float(input("Please enter the weight of your dimes: "))
quarters_weight = float(input("Please enter the weight of your quarters: "))
half_weight = float(input("Please enter the weight of your half dollars: "))
dollars_weight = float(input("Please enter the weight of your dollar coins: "))

# Calculates the amount of coins of each type!  Divides by weight of each coin and rounds to nearest full coin.

pennies = int(pennies_weight / 2.5)
nickels = int(nickels_weight / 5)
dimes = int(dimes_weight / 2.268)
quarters = int(quarters_weight / 5.670)
half = int(half_weight / 11.340)
dollars = int(dollars_weight / 8.1)

# Calculates the wrappers the user will need.
penny_wrappers = int(pennies / 50)
nickel_wrappers = int(nickels / 40)
dime_wrappers = int(dimes / 50)
quarter_wrappers = int(quarters / 40)
half_wrappers = int(half / 20)
dollar_wrappers = int(dollars / 25)

# Calculates the total dollar value of the coins.
total_value = (pennies * 0.01) + (nickels * 0.05) + (dimes * 0.1) + (quarters * 0.25) + (half * 0.5) + dollars

# Prints the quantity of each coin
print('You have: \n %s Pennies \n %s Nickels \n %s Dimes \n %s Quarters \n %s Half-Dollars \n %s Dollar Coins' \
    % (pennies, nickels, dimes, quarters, half, dollars))

# Prints the amount of wrappers of each type.
print('You need: \n %s Pennie wrappers \n %s Nickel wrappers \n %s Dime wrappers \n %s Quarter wrappers\
    \n %s Half-Dollar wrappers \n %s Dollar Coin wrappers' \
    % (penny_wrappers, nickel_wrappers, dime_wrappers, quarter_wrappers, half_wrappers, dollar_wrappers))

# Prints the total amount of money
print('You have a total of $%s.' % (total_value))








