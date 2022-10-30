#################################################################
# FILE : math_print.py
# WRITER : Omer Dahan , omerdahan , 315466664
# EXERCISE : intro2cs1 ex1 2023
# DESCRIPTION: A simple program that making some basic math calculations
# STUDENTS I DISCUSSED THE EXERCISE WITH: 
# WEB PAGES I USED: https://he.wikipedia.org/wiki/%D7%99%D7%97%D7%A1_%D7%94%D7%96%D7%94%D7%91
# NOTES: ...
#################################################################
# Importing the library math
import math
def golden_ratio(): 
    """This function calculate and prints gold ratio.
    using the golden ratio formula from wikipedia"""
    # Calculating and printing the golden ratio according to the formula
    print((1 + 5**0.5) / 2)
def six_squared():
    """This function calculates and prints 6 squared"""
    # Math.pow(x,y) calculates the x power of y
    print(math.pow(6, 2))
def hypotenuse():
    """This function calculates the hypotenuse of triangle 
    his sides are equal to 5 and 12"""
    # Combination of sqrt and pow(see description above)
    # Prints the calculation of the hypotenuse
    print((math.pow(5, 2) + math.pow(12, 2)) ** 0.5)
def pi():
    """This function prints the constant pi"""
    # prints pi with Math.pi returns the constant pi
    print(math.pi)
def e():
    """This function print the constant e"""
    # Prints e with math.e returns the constant e
    print(math.e)
def squares_area():
    """This functio prints all square areas whose theirs sides equal to 1-10"""
    #Using math.pow() to calculate the areas
    print(math.pow(1, 2),math.pow(2, 2),math.pow(3, 2),math.pow(4, 2),
    math.pow(5, 2),math.pow(6, 2),math.pow(7, 2),math.pow(8, 2),
    math.pow(9, 2),math.pow(10, 2))

# Calling to the function draw_fleet and finishing with turtle.done
# when this file is the main file
if __name__ == "__main__":
    golden_ratio()
    six_squared()
    hypotenuse()
    pi()
    e()
    squares_area()

