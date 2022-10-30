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
        return None 
    #cheks if the discriminantis equal to 0
    #If the discriminant is equal to 0 there is just one solution
    elif discriminant == 0:
        #calculates the solution
        sol1 = -b / 2*a
        #Return the one solution and also a None value as requested
        return sol1,None
    #If the first two options are not true so the discriminant is positive and
    #we have two solution and we will calculate them
    else:
        sol_1 = (-b + (discriminant ** 0.5)) / 2*a
        sol_2 = (-b - (discriminant ** 0.5)) / 2*a
        #return the values of both solutions
    return sol_1,sol_2


if __name__ == '__main__':
    print(quadratic_equation(-1, -5, 10))

