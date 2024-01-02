"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    #set the bounds for the search
    left_bound = 0
    right_bound = len(input_array) - 1
    while left_bound <= right_bound:
        middle_index = (left_bound + right_bound)//2
        #the value falls in the middle of search space
        if value == input_array[middle_index]:
            return middle_index
        #the value falls to the right of the search space as it is larger
        elif value > input_array[middle_index]:
            left_bound = middle_index + 1
        #the value falls to the left of the search space as it is smaller
        elif value < input_array[middle_index]:
            right_bound = middle_index - 1
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print (binary_search(test_list, test_val1))
print (binary_search(test_list, test_val2))