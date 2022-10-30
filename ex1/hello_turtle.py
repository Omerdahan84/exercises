#################################################################
# FILE : hello_turtle.py
# WRITER : Omer Dahan , omerdahan , 315466664
# EXERCISE : intro2cs1 ex1 2023
# DESCRIPTION: A simple program that draw two ships with three sails each
# STUDENTS I DISCUSSED THE EXERCISE WITH:  Ori Saas
# WEB PAGES I USED: 
# NOTES: ...
#################################################################

import turtle


def draw_triangle():
    """This function draw a triangle.
    Any section make a side of the triangle"""
    #1
    turtle.forward(45)
    turtle.right(120)
    #2
    turtle.forward(45)
    turtle.right(120)
    #3
    turtle.forward(45)
    turtle.right(120)
def draw_sail():
    """This function draw a sail"""
    #This part drawing the pole of the sail
    turtle.left(90)
    turtle.forward(50)
    turtle.right(150)
    #This part drawing the sail itself
    draw_triangle()
    turtle.right(30)
    #Moving the turtle back to a position that we can keep draw the ship
    turtle.up()
    turtle.forward(50)
    turtle.down()
    turtle.left(90)
def draw_ship():
    """This function is drawing a whole ship"""
    #Adjust the turtle to the right 
    turtle.right(90)
    #Drawing the deck before sail 1
    turtle.forward(50)
    #Draw sail 1
    draw_sail()
    #Drawing the deck between sail 1st and sail 2nd
    turtle.forward(50)
    #Draw sail 2
    draw_sail()
    #Drawing the deck between sail 2nd and sail 3rd
    turtle.forward(50)
    #Draw sail 3
    draw_sail()
    #Draw the deck between the 3rd sail and the right edge
    turtle.forward(50)
    #Drawing rigth edge
    turtle.right(120)
    turtle.forward(20)
    #Drawing lower deck
    turtle.right(60)
    turtle.forward(180)
    #Drawing left edge
    turtle.right(60)
    turtle.forward(20)
    #Finishing with arrow pointing right
    turtle.right(30)
def draw_fleet():
    """This function draw a fleet of two ships"""
    #Adjust the turtle so the draw ship function will draw currectly
    turtle.left(90)
    #Draw ship number 1
    draw_ship()
    #Adjust the turtle 90 degrees to the left to start the 2nd ship
    turtle.left(90)
    #Taking the turtle up so it's movment won't draw
    turtle.up()
    #Moving turtle to the starting possession as required to draw ship 2
    turtle.forward(300)
    #Adjust the turtle to looking up
    turtle.right(90)
    #Put down turtle so it's can draw
    turtle.down()
    #Draw ship number 2
    draw_ship()
    #Moving turtle up so we can move it without drawing
    turtle.up()
    #Move the turtle to the required finishing possession
    turtle.right(90)
    turtle.forward(300)

if __name__ == "__main__" :
    draw_fleet()
    turtle.done()

