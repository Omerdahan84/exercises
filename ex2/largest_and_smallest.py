#################################################################
# FILE : largest_and_smallest.py
# WRITER : Omer Dahan , omerdahan , 315466664
# EXERCISE : intro2cs1 ex2 2023
# DESCRIPTION:This program gets three numbers and returns the biggest
# and the smallest one
#################################################################
#I choose test 4 to be equal to (-11,-5,0) to see that the function
#is good to special number (negative,float,zero)
# I choose test 5 to be equal to (0, 5.4, 5.4) to check the case 
#of two equal maximum.
def largest_and_smallest(n1, n2, n3):
    """This function gets three numbers and returns the smallest
    and biggest value among them"""
    # Sets the intial value of the maximun to n1
    max_val = n1
    # if n2 is bigger we set the maximim to be n2
    if n2 > max_val:
        max_val = n2
    # if n3 is bigger we set the maximum to be n3
    if n3 > max_val:
        max_val = n3
    # Sets the intial value of the minimum to n1
    min_val = n1
    # if n2 is smaller from the min_value we set min_val to be
    # equal to =n2
    if n2 < min_val:
        min_val = n2
    # if n3 is smaller from the initial value we set min_val to be
    # equal to n3
    if n3 < min_val:
        min_val = n3
    return max_val,min_val
def check_largest_and_smallest():
    """This function test the function largest_and_smallest
    the function runs the largest_and_smallest function and
    return True If the returned values are equal to the values 
    she expected and false else """
    # Sets the values of max_val,min_val in accordance
    # to the values the calling gives back
    max_val, min_val = largest_and_smallest(17, 1, 6)
    # checks if the values the function gave back are
    # equal to expected values
    # 1
    if max_val != 17 or min_val != 1:
        # if the values are not equal to expected the function
        # return False
        return False 
        # If first test passed continue to next test
    else:
        # Sets new values to max_val and min_val for new calling
        max_val, min_val = largest_and_smallest(1, 17, 6)
        # 2
        # checks if the values the function gave back are
        # equal to expected values
        if max_val != 17 or min_val != 1:
            # if the values are not equal to expected the function
            # return False
            return False 
            # If second test passed continue to next test
        else:
            # Sets new values to max_val and min_val for new calling
            max_val, min_val = largest_and_smallest(1, 1, 2)
            # 3
            # checks if the values the function gave back are
            # equal to expected values
            if max_val != 2 or min_val != 1:
                # if the values are not equal to expected the function
                # return False
                return False 
            # If second test passed continue to next test
            else:
                # Sets new values to max_val and min_val for new calling
                max_val, min_val = largest_and_smallest(-11.4, -5.5, 0)
                # 4
                # checks if the values the function gave back are
                # equal to expected values
                if max_val != 0 or min_val != -11.4:
                    # if the values are not equal to expected the
                    # function return False
                    return False 
                else:
                    # Sets new values to max_val and min_val for new 
                    # calling
                    max_val, min_val = largest_and_smallest(0, 5.4, 5.4)
                # 5
                # checks if the values the function gave back are
                # equal to expected values
                if max_val != 5.4 or min_val != 0:
                    # if the values are not equal to expected the
                    # function return False
                    return False 
                else:
                    # If all test passed return true
                    return True
