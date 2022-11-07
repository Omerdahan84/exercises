def input_list():
    """This function get inputs of numbers from the user
    and return a list of numbers with the sum of the numbers as the
    last value of the list"""
    list_of_inputs = [] # initializing  new list
    # This loop takes inputs from the user,and adds the inputs to the end 
    # of the list. if the user enters an 
    # empty string the loop will stop
    while True:
        user_input = input()
        if user_input == '':
            break
        else:
            user_input = float(user_input)
            list_of_inputs.append(user_input)

    sum = 0 #initializing sum for adding the elements of the list
    # This loop going over the elements of the list and adds them together 
    for i in range(len(list_of_inputs)):
        sum += list_of_inputs[i]
    list_of_inputs.append(sum) # Adds the sum to the list
    return list_of_inputs

def inner_product(vec_1,vec_2):
    """This function gets two lists represent vectors and gives back
    their ineer porduct"""
    sum = 0 # initializing sum 
    LENGTH_1 = len(vec_1) # Storing the length of vec_1 as a constant
    LENGTH_2 = len(vec_2) # Storing the length of vec_2 as a constant
    # Checks if the lengths are inequal and return None if true
    if LENGTH_1 != LENGTH_2:
        return None
    # Checks if the lists are empty and return 0 if true
    if LENGTH_1 == 0 and LENGTH_2 == 0:
        return 0 
    # This loops going over the elements of both vectos and stores the 
    # product into sum 
    for i in range(LENGTH_1):
        sum += vec_1[i] * vec_2[i]
    return sum

def sequence_monotonicity(sequence):
    """This function gets a list represent a squence and return
    to which of the definitions of in the question this 
    sequence is appropriate in boolean list form =[def1,def2..]"""
    LENGTH = len(sequence) # Storing the length of the squence in
    # constant
    # Initializing boolean to put in the list of the defintions
    mono_up = True
    mono_up_strong = True
    mono_down = True
    mono_down_strong = True 
    list_of_definitions = [mono_up, mono_up_strong, mono_down,
    mono_down_strong]# Initializing list of defintions when all 
    # starting values are equal to true
    # Returns all true if the list is empty or has one value
    if LENGTH == 1 or LENGTH == 0:
        return list_of_definitions
    # Checks if every value fitting to defintion number 1
    # updated defintion number 1 to false if not
    for i in range(LENGTH - 1):
        if sequence[ i + 1] >= sequence[i]:
            pass
        else:
            list_of_definitions[0] = False
            break
    # Checks if every value fitting to defintion number 2
    # updated defintion number 2 to false if not
    for i in range(LENGTH - 1):
        if sequence[ i + 1] > sequence[i]:
            pass
        else:
            list_of_definitions[1] = False
            break    
    # Checks if every value fitting to defintion number 3
    # updated defintion number 3 to false if not    
    for i in range(LENGTH - 1):
        if sequence[ i + 1] <= sequence[i]:
            pass
        else:
            list_of_definitions[2] = False
            break
    # Checks if every value fitting to defintion number 4
    # updated defintion number 4 to false if not    
    for i in range(LENGTH - 1):
        if sequence[ i + 1] < sequence[i]:
            pass
        else:
            list_of_definitions[3] = False
            break    
    return list_of_definitions

def monotonicity_inverse(def_bool):

    """This function gets a list of sequence defenitions and 
    returns a list the fits to the definition if """
    # Checks if the definition ask for a sequence that goes up 
    # and down in the same time or all
    # definition equal to false and returns None if true
    if (def_bool[0] == True or def_bool[1] == True) and\
    (def_bool[2] == True or def_bool[3] == True) or\
    (def_bool == [False, False, False, False]):
        return None
    # checks the definition and return a list that fit
    # to each one
    if def_bool[0] == True and def_bool[1] == True:
        return [1, 2, 3, 4]
    if def_bool[0] == True and def_bool[1] == False: 
        return [1, 1, 3, 4]   
    if def_bool[2] == True and def_bool[3] == True:
        return [4, 3, 2, 1]
    if def_bool[2] == True and def_bool[3] == False:
        return [4, 3, 2, 2]

def convolve(mat):
    LENGTH_MAT = len(mat)
    if LENGTH_MAT == 0:
        return None
    sum = 0
    table = []
    for i in range(LENGTH_MAT):
        row = []
        for j in range(len(mat[i])):
            sum = 0
            for x in range(-1,3):
                for y in range(-1,3):
                    current_x = i + x
                    current_y = j + y
                    if current_x < 0 or current_x > LENGTH_MAT-1\
                    or current_y < 0 or current_y > len(mat[i])-1:
                        continue
                    sum += mat[current_x][current_y]
            row.append(sum)
        table.append(row)
    return table 

def sum_of_vectors(vec_lst):
    """This function gets a list of lists represent vectors and gives back
    the some of all of this vectors"""
    # Checks if there are no vectors
    if len(vec_lst) == 0:
        return None
    # Checks if the vectros are not empty
    for i in range(len(vec_lst)):
        if len(vec_lst[i]) == 0:
            return None
    sum_v = [] # Initializing the vectors of the sums
    sum = 0 # Initializing sum 
    j = 0  # Initializing j 
    # This block going over the cloumns of the matrix
    # to give back the sum
    for i in range (len(vec_lst[j])):
        sum = 0
        for j in range(len(vec_lst)):
            sum  += vec_lst[j][i]
        sum_v.append(sum)
    return sum_v
assert sum_of_vectors([[1, 1], [1, 3]])

assert sum_of_vectors([[1, 1, 1], [1, 0, 0], [0, 0, 100]]) 

assert sum_of_vectors([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
