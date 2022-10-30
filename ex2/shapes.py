#Importing the library math
import math

def shape_area():
    """This function will prompt the user to choose the kind of
    shape he want to calculate it's area. After receiving the input 
    the function will calculate the area according to the formula of area
    for the shape the user choosed"""
    #This line prompt the user to choose a shape
    #the user choose by entering a number according 
    #to the message he receives
    user_input = input("Choose shape (1=circle, 2=rectangle, 3=triangle): ")
    #Checks if the user input equal to '1'
    if user_input == '1':
        #storing the value of the radius of the circle
        #it's necessary to cast the input because it's type is str
        #which not allow numeric calculations
        radius = float(input())
        #returns the area of a circle according to circle area formula
        return math.pi * radius**2
    #Checks if the inputs is equal to '2'
    elif user_input == '2':
        #storing the values of the sides of the trctangle 
        #necessary to cast - same reason as before
        first_side = float(input())
        second_side = float(input())
        #returns and calculates the area according to the formula
        return first_side * second_side
    #check if user input is equal to 3
    elif user_input == '3':
        #storing the value of the side of the triangle
        #casting for the same reason as the first condition
        side = float(input())
        #return the value of area according to the formula of triangle
        #with equal sides
        return (3**0.5 / 4) * side**2
