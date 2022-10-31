import math

def shape_area():
    user_input = input("Choose shape (1=circle, 2=rectangle, 3=triangle): ")
    if user_input == '1':
        radius = float(input(("Insert the radius of the circle: ")))
        return math.pi * radius**2
    elif user_input == '2':
        first_side = float(input(("Insert the first side of the rectangle: ")))
        second_side = float(input(("Insert the second side of the rectangle: ")))
        return first_side * second_side
    elif user_input == '3':
        side = float(input(("Insert the side of the triangle: ")))
        return (3**0.5 / 4) * side**2

