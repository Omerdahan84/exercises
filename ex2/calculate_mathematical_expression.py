def calculate_mathematical_expression(n1, n2, operator):
    """"This function gets two numbers and an operator and returns the 
    value obtained from applying the opreator to the numbers"""
    #If the opreator is plus, the function will return the sum
    #of the numbers
    if operator == '+':
        return n1 + n2
    #If operator is minus, the function will subtract the first number
    #from the second  
    elif operator == '-':
        return n1 - n2
    #If operator is asterisk, the function will return the multiplier
    #the numbers
    elif operator == '*':
        return n1* n2
    #If operato is colon, the function will return the division of the
    #the first number by the second
    #if the number n2 is equal to zero the function will return none Value for
    #division
    elif operator == ':' and n2 != 0:
        return n1/n2
    else:
        #If the operator is not any of {'+' ,'-' ,'*' ,':'} the
        #function will return None
        return None