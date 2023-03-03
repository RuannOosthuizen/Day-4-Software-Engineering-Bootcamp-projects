# Here I am using the input function to ask the user to input three different integer numbers. then storing those values into varbiables called num1, num2 and num3.
# I am also using the casting method to change the string variables into integers this is done by adding the int() funtion to the input() funtion.
num1 = int(input("Please enter a whole number:\n "))
num2 = int(input("Please enter a second whole number:\n "))
num3 = int(input("Then lastly please enter a third whole number:\n "))

# Here I am using the mathematical operation functions of adding the three varaibles together
# by simply using the symbol "+" to add them together intoa whole new number and saving that data in a variable called addition_num.
# and then printing that variable out.
addition_num = num1 + num2 + num3
print("Here is the sum of all three numbers you have inputted:")
print(addition_num)

# Here I am subtracting the first number with the second number using the subraction symbol "-",
# and then saving that data in a varaible called subtraction_num, then printing it out.
subtraction_num = num1 - num2
print("Here is your first number minus the second number:")
print(subtraction_num)

# Here I am multiplying the the value the user has inputted with the first value the user has inputted. Then saving that data in a variable called multiplied_num, then printing it.
multiplied_num = num3 * num1
print("Here is your 3rd number multiplied by the first number:")
print(multiplied_num)

# Here I am recaling the sum of all three numbers i previously stored in variable called addition_num
# and then dividing it by the third value the user has inputted using the sumbol "/", then storing that value in a variable called deivision_num and printing it.
division_num = addition_num / num3
print("And then lastly here is the sum of all three numbers devided by your third number:")
print(division_num)