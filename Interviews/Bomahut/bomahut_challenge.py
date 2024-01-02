"""
a) Write an algorithm that given an M X N  matrix return all numbers that are the maximum value in its row but the minimum in its column
For example if given the matrix
Input:matrix = [[5,16,20],[9,11,18],[15,16,17]]
Output:[17]
Explanation:17 is the only number since it is the maximum in its row and the minimum in its
column.
Input:matrix = [[100,60,20, 50],[70,80,10,90],[10,50,44,30]]
Output:[50]
Explanation:50 is the only number since it is the maximum in its row and the minimum in its
column.
Constraints:
● m == mat.length
● n == mat[i].length
● 1 <= n, m <= 50
● 1 <= matrix[i][j] <= 105.
● All elements in the matrix are distinct.
b) What is the space and time complexity of your solution?
c) Write 1-2 tests that you run to validate your answer.
"""
#SOLUTION
"""
1) Interpretation of constraints (The name of the matrix is assumed to be mat):
● m == mat.length => the number of rows equal the length of the matrix
● n == mat[i].length => the number of columns equal the length of the individual row (rectangular matrices are thus allowed)
● <= n, m <= 50 => the number of rows and columns for the matrix should be between 1 and 50
● 1 <= matrix[i][j] <= 105 =>the elements in the rows and columns of the matrix should be between 1 and 105
"""
"""
2) Pseudo code steps
● Loop through all the rows of the matrix
● Get the maximum element of the last row and its column
● Get the maximum element in the current row
● Loop through the subsequent rows of the matrix
● Check if the maximum element in the current row is the minimum element in the whole column
● Append that element in the list to return
● Check that the maximum element of the last row is also the minimum element in the whole column
"""
def max_row_min_column(matrix:list)->list:
    max_row_min_col = list()
    len_matrix = len(matrix)
    #get the maximum element in the last row and its index for the last step comparison
    last_col = list()
    max_last_row = max(matrix[len_matrix-1])
    index_of_max_last_row = matrix[len_matrix-1].index(max_last_row)
    # Iterate over each row in the matrix
    for i in range(len_matrix):
        #Obtain the maximum number in the row and its index
        max_row_num = max(matrix[i])
        max_row_min_col.append(max_row_num)
        index_of_max_row_num = matrix[i].index(max_row_num)
        #append the elements in the columns corresponding to the maximum element in the last row
        #since I do not iterate backwards to compare it with its previous
        last_col.append(matrix[i][index_of_max_last_row])
        #loop over subsequent rows and check if this element is the minimum
        for j in range(i+1,len_matrix):
            #if it is greater than any element, remove it from the list to be returned, and break out of loop
            if max_row_num > matrix[j][index_of_max_row_num]:
                max_row_min_col.remove(max_row_num) 
                break  
        #check that the maximum element in the last row is also the minimum element in its column
        if i == len_matrix -1:
            if max_last_row in max_row_min_col:
                if min(last_col) != max_last_row:
                    max_row_min_col.remove(max_last_row)
    return max_row_min_col
#Test with [[5,16,20],[9,11,18],[15,16,17]]->17
print(max_row_min_column(matrix=[[5,16,20],[9,11,18],[15,16,17]]))
#Test with [[100,60,20, 50],[70,80,10,90],[10,50,44,30]]->50
print(max_row_min_column(matrix=[[100,60,20, 50],[70,80,10,90],[10,50,44,30]]))
"""c) TESTS"""
#Test for none of the elements matrix[i][j] qualifying the conditions of max row, min column
#Test matrix = [[85,86,87,88],[84,81,78,75],[83,80,77,74],[73,79,76,82]]->[]
print(max_row_min_column(matrix=[[85,86,87,88],[84,81,78,75],[83,80,77,74],[73,79,76,82]]))

"""b) SPACE & TIME COMPLEXITY"""
"""
● The space complexity of the algorithm is 0(1) since I did not create any new matrix during the iterations
● The time complexity is derived as follows (assuming the whole array length is n):
1. The outer for loop for the rows goes through the whole array hence it is 0(n)
2. The inner for loop for the subsequent rows goes through the array one less time, for every outer call hence tabulated we have
---------------------------------------------------------------------
m | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | n |
----------------------------------------------------------------------
n | 0 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9  | 10 | 11 | n-1 |

Hence given the arithmetic series, and then it will be 0(n*n^2) = 0(n^3) worst case
● It is not possible to make this array more efficient than this as the algorithm must examine every element at least once
to determine which elements are maximum in their row and minimum in their columns.
● The improvement I made in this algorithm was by checking if at least one of the elements satisfies the conditions in which case
I do not check the whole matrix. This can improve the average case performance.
"""
