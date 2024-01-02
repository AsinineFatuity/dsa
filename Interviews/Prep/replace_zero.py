# Given an array containing None values fill in the None values with most recent 
# non None value in the array 
array1 = [1,None,2,3,None,None,5,None]

def replace_zero_(array:list)->list:
    valid = 0
    for idx in range(len(array)):
        if array[idx] is not None:
            valid = array[idx]
        else:
            array[idx] = valid
    return array

print(replace_zero_(array1))