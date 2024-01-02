"""
Implement quick sort in Python.
Input a list. Output a sorted list.
"""
#this only manages to partition and its space complexity is also awesome
def quicksort(array)->list:
    high_index = len(array)-1
    low_index = 0
    if low_index >= high_index:
        return
    pivot = array[high_index]
    left_pointer = low_index
    right_pointer = high_index
    while left_pointer < right_pointer:
        #Walk from the left until we find a number greater than the pivot, or hit the right pointer
        while array[left_pointer] <= pivot and left_pointer < right_pointer:
            left_pointer += 1
        #Walk from the right until we find a number less than the pivot, or hit the left pointer.
        while array[right_pointer] >= pivot and left_pointer < right_pointer:
            right_pointer -= 1

        swap_holder = array[left_pointer]
        array[left_pointer] = array[right_pointer]
        array[right_pointer] = swap_holder
    #the left equals the right pointer
    if array[left_pointer] > array[high_index]:
        swap_holder = array[left_pointer]
        array[left_pointer] = pivot
        array[high_index] = swap_holder
    else:
        left_pointer = high_index
    #recursively sort the left and right of pivot
    pivot_index = array.index(pivot)
    # quicksort(array[:pivot_index])
    # quicksort(array[:pivot_index+1])
    return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print (quicksort(test))