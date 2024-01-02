"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
from random import randint
def quicksort(array):
    len_array = len(array)
    if len_array <= 1:
        return array
    else:
        #chose pivot at random to avoid worst case scenario O(n^2) if the array is nearly normally/reversely sorted
        pivot = array[randint(0,len_array-1)]
    items_left = [item for item in array if item < pivot]
    items_right = [item for item in array if item > pivot]
    items_middle = [item for item in array if item == pivot]
    return quicksort(items_left) + items_middle + quicksort(items_right)

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print (quicksort(test))