"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""
#pse
"""

"""
def find_two_nums(array:list,target:int)->list:
    num_2 = 0
    for i in range(len(array)):
        num_2 = target - array[i]
        try:
            num_2_idx = array.index(num_2,i+1)
            return [i,num_2_idx]
        except:
            pass
    return [i,num_2_idx]

print (find_two_nums([2,7,11,15],9)) 
print(find_two_nums([3,2,4],6))     
