import ex7_helper as helper
from typing import *
import copy

def mult(x: helper.N, y: int) -> helper.N:
    """takes an int or float and return the product of the two numbers
     :param:x,y , y is an int
     :return x*y"""

    if y == 0:
        return 0
    else:
        # adding x and substruct y
        return helper.add(x, mult(x, helper.subtract_1(y)))


def is_even(n: int) -> bool:
    """takes an int and return true if even and false else
    :param n
    :return True,False"""
    if n == 0:
        return True
    elif n == 1:
        return False
    else:
        # substruct 2 from the number
        return is_even(helper.subtract_1(helper.subtract_1(n)))


def log_mult(x: Union[int, float], y: int) -> Union[int, float]:
    """this function calculates the product of x and y in log(n) complexity
    :param: x,y x is float or int y is int
    :return: product of x and y"""
    if y == 0:
        return 0
    elif y == 1:
        return x
    # if y is odd we're making normal mult
    elif helper.is_odd(y):
        return helper.add(x, log_mult(x, helper.subtract_1(y)))
    else:
        # if y is even we will divide y by 2 and making the mult on 2x
        return log_mult(helper.add(x, x), helper.divide_by_2(y))

def is_power(b: int, x: int) -> bool:
    if b == 1:  # Check special cases
        return x == 1
    elif b == 0:
        return x == 1 or x == 0
    elif x==0 or b ==0 :
        return False
    return is_power_helper(1, b, x)
def is_power_helper(counter:float, b:int, x:int)->bool:
    if counter == x:
        return True
    elif counter > x:
        return False
    else:
        return is_power_helper(log_mult(counter, b), b, x) # mul is our special multiplication function


def reverse(s: str) -> str:
    """Reverses a given string.

    Args:
        s: The string to reverse.

    Returns:
        The reversed string.
    """

    # Helper function that reverses the substring starting at the current position and ending at the end of the string
    def reverse_substring(curr: int, end: int) -> str:
        """Reverses the substring of the given string starting at the current position and ending at the end of the string.

        Args:
            curr: The current position in the string.
            end: The end of the string.

        Returns:
            The reversed substring.
        """
        # Base case: if the current position is at the end of the string, return an empty string because an empty
        # string is its own reverse
        if curr >= end:
            return ''

        # Recursive case: reverse the substring that comes after the current character of the string
        return helper.append_to_end(reverse_substring(helper.add(curr, 1), end), s[curr])

    # Return the reversed string by calling the helper function with pointers to the start and end of the string
    return reverse_substring(0, len(s))


def play_hanoi(hanoi: Any, n: int, src: Any, dest: Any, temp: Any) -> None:
    """Solves the Tower of Hanoi puzzle for a given number of disks.

    Args:
        hanoi: An object representing the current state of the puzzle.
        n: The number of disks in the puzzle.
        src: The peg to move the disks from.
        dest: The peg to move the disks to.
        temp: The peg to use as a temporary location.

    Returns:
        None. The function updates the state of the puzzle using the `hanoi.move` method.
    """
    if n < 1:
        return None
    if n == 1:
        hanoi.move(src, dest)

    else:
        play_hanoi(hanoi, helper.subtract_1(n), src, temp, dest)
        hanoi.move(src, dest)
        play_hanoi(hanoi,helper.subtract_1(n), temp, dest, src)
def number_of_ones_helper(n: int, count: int) -> int:
    """return a number of ones for a specific integer"""
    if n == 0:
        return count
    else:
        #if the last digit is equal to one we wiil increment count
        if n % 10 == 1:
            count += 1
            #calling to the function with the next digit
        return number_of_ones_helper(n // 10, count)
def number_of_ones(n: int) -> int:
    """for each number from 1 to n we calculate the number of ones"""
    if n == 0:
        return  0
    return  number_of_ones(n-1)+number_of_ones_helper(n,0)
def compare_2d_lists(l1: List[List[int]], l2: List[List[int]]) -> bool:
    # Base case: if the length of the two external lists is different, the lists are not equal
    if len(l1) != len(l2):
        return False

    # Check if the outer lists are empty
    if len(l1) == 0 and len(l2) == 0:
        return True

    # Check if the inner lists are empty
    if len(l1) == 0 or len(l2) == 0:
        return False

    # Recursive case: compare the first sublist of l1 with the first sublist of l2, and
    # compare the rest of the sublists recursively
    return compare_2d_lists_helper(l1, l2, 0, 0)

def compare_2d_lists_helper(l1: List[List[int]], l2: List[List[int]], i: int, j: int) -> bool:
    # Base case: if we have reached the end of the outer lists, the lists are equal
    if i == len(l1) and j == len(l2):
        return True

    # If we have reached the end of one of the outer lists, but not the other, the lists are not equal
    if i == len(l1) or j == len(l2):
        return False

    # Recursive case: compare the current sublist of l1 with the current sublist of l2, and
    # move on to the next sublists
    return compare_1d_lists(l1[i], l2[j]) and compare_2d_lists_helper(l1, l2, i + 1, j + 1)

def compare_1d_lists(l1: List[int], l2: List[int]) -> bool:
    # Base case: if the length of the two internal lists is different, the lists are not equal
    if len(l1) != len(l2):
        return False

    # If the length of the internal lists is zero, the lists are equal (since they are empty)
    if len(l1) == 0:
        return True

    # Recursive case: compare the first elements of the two lists, and compare the rest of the lists
    # recursively
    return compare_1d_lists_helper(l1, l2, 0, 0)
def compare_1d_lists_helper(l1: List[int], l2: List[int], i: int, j: int) -> bool:
    # Base case: if we have reached the end of the inner lists, the lists are equal
    if i == len(l1) and j == len(l2):
        return True

    # If we have reached the end of one of the inner lists, but not the other, the lists are not equal
    if i == len(l1) or j == len(l2):
        return False

    # Recursive case: compare the current elements of the lists, and move on to the next elements
    return l1[i] == l2[j] and compare_1d_lists_helper(l1, l2, i + 1, j + 1)

def magic_list(n: int) -> List[Any]:
    """this function return a sequence of an empty lists according to rules in ex7 """
    #base case
    if n == 0:
        return []
    else:
        #recursive case, adding the next item in the sequence
        return magic_list(helper.subtract_1(n)) + [magic_list(helper.subtract_1(n))]
