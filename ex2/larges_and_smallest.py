def largest_and_smallest(n1, n2, n3):
    """This function gets three numbers and returns the smallest
    and biggest value among them"""
    max_val = n1

    if n2 > max_val:
        max_val = n2
    if n3 > max_val:
        max_val = n3

    min_val = n1

    if n2 < min_val:
        min_val = n2
    if n3 < min_val:
        min_val = n3
    return max_val,min_val

if __name__ == '__main__':
    max_val, min_val = largest_and_smallest(155, 11, 11)
    print(max_val) # result is 10
    print(min_val) # result is 1
