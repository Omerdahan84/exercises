#################################################################
# FILE : math_print.py
# WRITER : Omer Dahan , omerdahan , 315466664
# EXERCISE : intro2cs1 ex1 2023
# DESCRIPTION: A simple program that making some basic math calculations
# STUDENTS I DISCUSSED THE EXERCISE WITH: 
# WEB PAGES I USED: https://he.wikipedia.org/wiki/%D7%99%D7%97%D7%A1_%D7%94%D7%96%D7%94%D7%91
# NOTES: ...
#################################################################
from cmath import sqrt
import math
def golden_ratio(): 
    """This function calculate and prints gold ratio.
    using the golden ratio formula from wikipedia"""
    #Math.sqrt(x) =  give back the square root of x
    print(str((math.sqrt(5) + 1) / 2))
def six_squared():
    """This function calculates and prints 6 squared"""
    #Math.pow(x,y) calculates the x power of y
    print(math.pow(6, 2))
def hypotenuse():
    """This function calculates the hypotenuse of triangle 
    his sides are equal to 5 and 12"""
    #Combination of sqrt and pow(see description above)
    print(str(math.sqrt(math.pow(5, 2) + math.pow(12, 2))))
def pi():
    """This function prints the constant pi"""
    #Math.pi returns the constant pi
    print(math.pi)
def e():
    """This function print the constant e"""
    #Math.e returns the constant e
    print(math.e)
def squares_area():
    """This functio prints all square areas whose theirs sides equal to 1-10"""
    #Using math.pow() to calculate the areas
    print(math.pow(1, 2),math.pow(2, 2),math.pow(3, 2),math.pow(4, 2),
    math.pow(5, 2),math.pow(6, 2),math.pow(7, 2),math.pow(8, 2),
    math.pow(9, 2),math.pow(10, 2))

if __name__ == "__main__":
    golden_ratio()
    six_squared()
    hypotenuse()
    pi()
    e()
    squares_area()

