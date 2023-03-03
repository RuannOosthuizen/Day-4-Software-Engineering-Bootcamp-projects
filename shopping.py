# Here I am using the input function to gather three values of their grocery list then storing those values in variables called item1, item2 and item3.
item1 = input("Please enter your first product to buy:\n")
item2 = input("Please enter the second prodcut you wish to buy:\n")
item3 = input("Please enter your third prodcut you wish to buy:\n")

# Here I am then asking the user to list the pricing of the product they have entered in using the input fucntion,
# then by using the float funtion to create the floating numbers and storing those values in variables called price1, price2 and price3.
price1 = float(input(f"Please enter the pricing of item {item1}: for example Chicken is R25.99:\n R"))
price2 = float(input(f"Please enter the pricing of item {item2}: for example Fish is R32.99:\n R"))
price3 = float(input(f"Please enter the pricing of item {item3}: for example Vegatibles are R21.99:\n R"))

# Here I am using the addition function symbol "+" to callutale the total amount the user would have to
# spend to buy all three items. I then save this value in a variable called total_amount.
total_amount = price1 + price2 + price3

# Here I am using the round function to caculate the average of all three product the user has entered in, then saving that value in a variable called average_amount.
# using the round function here will round up or down the total value making it easier to calculate the average for the total amount.
average_amount = round(price1 + price2 + price3)

# Here I am simply printing out the users infomation given about the products and giving the user the caculated values of the total amount and the averag amount they need to spend as instructed by the task sheet.
print(f"The total of {item1}, {item2} and {item3} is R{total_amount} and the average price of the items is R{average_amount}.")