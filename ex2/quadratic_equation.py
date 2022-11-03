# FILE : quadratic_equation.py
# WRITER : Omer Dahan , omerdahan , 315466664
# EXERCISE : intro2cs1 ex2 2023
# DESCRIPTION:This program gets from the user a coefficients of quadratic
# equation and return to the user the solutions to that equation
# Students I discussed with:
# Websites I used:https://docs.python.org/3.4/library/stdtypes.html#str.split
def quadratic_equation(a, b, c):
    """This function gets coefficients of a quadratic equation (where a 
    is the coefficient of x^2 and b is the coefficient of x and c is the free
    number) and returns the values of the solutions"""
    #This part is calculating the discriminant of the equation
    #the discriminant is the part under the square root in the formula 
    #of the quadratic equation
    discriminant = b ** 2 - (4 * a *c)
    #Checks if the value of the discriminant is negative, if it does
    #the equation has no solusion and we will return a None value
    if discriminant < 0:
        return None, None
    #cheks if the discriminantis equal to 0
    #If the discriminant is equal to 0 there is just one solution
    elif discriminant == 0:
        #calculates the solution
        sol1 = -b / (2*a)
        #Return the one solution and also a None value as requested
        return sol1, None
    #If the first two options are not true so the discriminant is positive and
    #we have two solution and we will calculate them
    else:
        sol_1 = (-b + (discriminant ** 0.5)) / (2*a)
        sol_2 = (-b - (discriminant ** 0.5)) / (2*a)
        #return the values of both solutions
    return sol_1,sol_2

def quadratic_equation_user_input():
    """This function gets the coefficients of a quadratic
    equation from the user, the function will return the
    value of the solutions of the equation"""
    # This line gets the user input
    user_input = input("Insert coefficients a, b, and c: ")
    # This line insert the input of the user to a list, using the function 
    # split we can to separate the values into different indexes 
    # for using them later
    input_list = user_input.split(' ')
    # This line checks if the coefficient of x^2 is not equal to 0 
    if input_list[0] == '0':
        # If the a parameter is equal to 0 the user will get this message
        print('The parameter \'a\' may not equal 0')
        # If the input is ok the function will sraet to calculate
    else:
        # Inserting the values of the solution into the variables sol_1,sol_2
        # We use the coefficients from the user input and calling the
        # function quadratic_equation to calculate for this 
        # specifics coefficients
        # Its necessary to cast the input because it's type value is str
        sol_1,sol_2 = quadratic_equation(float(input_list[0]), 
        float(input_list[1]),float(input_list[2]))
        # This condition checks if both of the solutions has numeric
        #values in that case it will print to the user the two solutions
        if sol_1 != None and sol_2 != None:
            print('The equation has 2 solutions: ' + str(sol_1) +' and ' + str(sol_2))
        # This section checks if one of the solutions is None, wich means that the equation has
        # one solution, in this case the function will print to the user the 1 solution
        elif sol_1 == None and sol_2 != None:
            print('The equation has 1 solution: ' + str(sol_2))
        elif sol_1 != None and sol_2 == None:
            print('The equation has 1 solution: ' + str(sol_1))
        # Getting here means both of the values has the value None
        # this means the equation has no solution 
        # the function will print it to the user
        else:
            print('The equation has no solutions')

if __name__ == '__main__':
    inp = ''
    while inp != "end":
        quadratic_equation_user_input()