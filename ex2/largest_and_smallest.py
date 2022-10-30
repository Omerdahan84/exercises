def largest_and_smallest(n1, n2, n3):
    """This function gets three numbers and returns the smallest
    and biggest value among them"""
    #Sets the intial value of the maximun to n1
    max_val = n1
    #if n2 is bigger we set the maximim to be n2
    if n2 > max_val:
        max_val = n2
    #if n3 is bigger we set the maximum to be n3
    if n3 > max_val:
        max_val = n3
    #Sets the intial value of the minimum to n1
    min_val = n1
    #if n2 is smaller from the min_value we set min_val to be
    #equal to =n2
    if n2 < min_val:
        min_val = n2
    #if n3 is smaller from the initial value we set min_val to be
    #equal to n3
    if n3 < min_val:
        min_val = n3
    return max_val,min_val
