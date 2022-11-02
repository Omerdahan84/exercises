#################################################################
# FILE : calculate_mathematical_expresiion.py
# WRITER : Omer Dahan , omerdahan , 315466664
# EXERCISE : intro2cs1 ex2 2023
# DESCRIPTION:This program gets a string from the user which represent
#calculation with the signs {'+' ,'-' ,'*' ,':'}  and return 
#the result of that caculation
#################################################################
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
        return n1 * n2
    #If operato is colon, the function will return the division of the
    #the first number by the second
    #if the number n2 is equal to zero the function will return none Value for
    #division
    elif operator == ':' and n2 != 0:
        return n1 / n2
    else:
        #If the operator is not any of {'+' ,'-' ,'*' ,':'} the
        #function will return None
        return None
def calculate_from_string(string_to_calc): 
    """This function gets a string presnt a calculation and
    return the value is obtained from thar calculation"""
    #Setting the intial value of opreator to empty string
    l = string_to_calc.split()
    #return the value from calculate_mathematical_expression when the values 
    #l[0],l[1] are the numbers obtained from the function split and the opreator is
    #the opreator we found earlier, we also casting l[0],l[1] because the return value
    #inside the list is strings.
    return calculate_mathematical_expression(float(l[0]), float(l[2]), str(l[1]))
if __name__ == '__main__':
    stirng = input()
    print(calculate_from_string(stirng))