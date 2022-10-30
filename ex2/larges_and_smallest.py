def largest_and_smallest(n1, n2, n3):
    """This function gets three numbers and returns the smallest
    and biggest value among them"""
    #This part checks if n1 is bigger than n2 and n3
    if n1 > n2 and n1 > n3:
        #if the answer is true n1 is tha maximum and we will set
        #max_val to be equal to n1
        max_val = n1
    #if n1 is not the biggest we need to check if n2 is bigger than n3
    elif n2 > n3:
        #if n2 is bigger the its the maximum and we will set
        #max_val to be equal to n
        max_val = n2 
    else:
        #if none of the above we have two options 
        #n3 is the maximum value or values are eaual
        #in any case we can set max_val to be equal to n3
        max_val = n3 
    #Check if n1 is smaller from both n1 and n3 if it's true so
    #n1 is the minimum
    if n1 < n2 and n1 < n3:
        #Sets min_val to be equal to n1 if the condition is true
        min_val = n1
    #check if n3 is bigger the n2
    elif n2 < n3:
        #sets the min_val to be equal to n2 if the condition is true
        min_val = n2 
    else:
        #if none of the above hppens we can infer n3 is smallest or
        #we have equal values
        #in any case we can ser min_val to be equal to n3 
        min_val = n3 
    return max_val,min_val

if __name__ == '__main__':
    max_val, min_val = largest_and_smallest(456443, -15, -52)
    print(max_val) # result is 10
    print(min_val) # result is 1
