# FILE : temperature.py
# WRITER : Omer Dahan , omerdahan , 315466664
# EXERCISE : intro2cs1 ex2 2023
# DESCRIPTION: This program gets thersold temperature and three 
# measurements. The function will return True value if two out of
# the three measurements are bigger than the threshold and false else
# Students I discussed with:
# Websites I used:
def is_vormir_safe(threshold, measurement1, measurement2, measurement3):
    """"This function gerts 4 parametrs thresold and three measurements
     of different days. The function return true if at least two out
     of the three are bigger than the threshold and false else"""
    #Checks if measurement1 and measurement2 are bigger than 
    #threshold
    if measurement1 > threshold and measurement2 > threshold:
        #If condition is true the function return True
        return True
    #if first condition is False. Checks if measurement1 and
    #measurement2 are bigger the threhold
    elif measurement1 > threshold and measurement3 > threshold:
        #If condition is true the function return True
        return True
    #if second condition is False. Checks if measurement2 and
    #measurement3 are bigger the threhold
    elif measurement2 > threshold and measurement3 > threshold:
        #If condition is true the function return True
        return True
    #if all three condition are False we didn't find 
    #values that are suitable to what we need
    else:
        #If all three condition are false the function will return
        #false
        return False