# Here I am colecting data of a triangle from the user by asking them to enter it in using the input function,
# then storing those values in variables called side1, side2 and side3.
# Note I am casting these values as floating numbers to gather the more accurate measurements, this is done by using the float function on the input function.
side1 = float(input("Please enter the lenght of the first side of the triangle:\n"))
side2 = float(input("Please enter the lenght of the second side of the triangle:\n"))
side3 = float(input("Please enter the lenght of the third and final side of the triangle:\n"))

# Here I am then using the data of the sides to calculate the semi-perimeter by using the equetion of adding all three sides devided by 2.
# Thus using the values the user gave for the triangle sides we can then use the addition symbol "+" and then
# deviding it by 2 using the division symbol "/" and saving that value in a variable called s for simplicity sake to make the final equetion easier on the eye.
# Note: by putting the users data in brackets, Python will first solve the equetion inside the brackets before moving on to solving the equetion outside the brackets.
s = (side1 + side2+ side3)/2

# Then by using the formula for are "are of triangle = (perimeter x (perimeter - side 1) x (perimeter - side 2) x (perimeter - side 3)) - 1/2".
# I can then tell Python to calculate the are by using the multiply, devide, minus and exponent symbols or functions to caculate the total area of the triangle.
# and then saving that value in a variable called area
area = (s*(s-side1)*(s-side2)*(s-side3))**0.5

# Here I am then (after a long brain melting session) simply printing out the final area in decimal factor of 2 format, using the modulo sumbol "%" and adding 0.2f to ge the remainder of the division.
# Note: I have removed the f-string symbol "f" to the modulo symbol "%0.2" to resolve errors that were showing up
#       when I placed the f-string symbol at the beginning as well as removing the curly brackets off from the variable "area" as this also produced an error.
print("The area of your triangle is %0.2f"%area)
