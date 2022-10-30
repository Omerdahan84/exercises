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
        #call the function circle are to calculate the area
        return circle_area(radius)
    #Checks if the inputs is equal to '2'
    elif user_input == '2':
        #storing the values of the sides of the trctangle 
        #necessary to cast - same reason as before
        first_side = float(input())
        second_side = float(input())
        #call the function rectangle_area to calculate the area
        return rectangle_area(first_side, second_side)
    #check if user input is equal to 3
    elif user_input == '3':
        #storing the value of the side of the triangle
        #casting for the same reason as the first condition
        side = float(input())
        #return the value of area according to the formula of triangle
        #with equal sides
        #call the function triangle_area to calculate the area
        return triangle_area(side)
        
def circle_area(radius):
    """This function gets a radius of a circle and return its area 
    according to the formula"""
    #returns the area of a circle according to circle area formula
    return math.pi * radius**2
def rectangle_area(first_side, second_side):
    """This function gets two sides of rectangle and returns
    it's area"""
    #returns and calculates the area according to the formula
    return first_side * second_side
def triangle_area(side):
    """This function gets the side of a triangle with equal sides
    and returns his area according to the formula"""
    return (3 ** 0.5 / 4) * side**2
