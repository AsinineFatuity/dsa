#QUESTION
"""
a) Write an algorithm that given an M X N  matrix return all numbers that are the maximum value in its row but the minimum in its column
For example if given the matrix
b) What is the space and time complexity of your solution?
c) Write 1-2 tests that you run to validate your answer.
"""
#INTERPRETATION(The name of the matrix is assumed to be mat)
"""
● m == mat.length => the number of rows equal the length of the matrix
● n == mat[i].length => the number of columns equal the length of the individual row (rectangular matrices are thus allowed)
● <= n, m <= 50 => the number of rows and columns for the matrix should be between 1 and 50
● 1 <= matrix[i][j] <= 105 =>the elements in the rows and columns of the matrix should be between 1 and 105
"""
#ASSUMPTION
"""
The test matrices are square, rectangular ones would be complex to handle and require help of libraries such as numpy
"""
#PSEUDO CODE STEPS
"""
● Declare empty list of valid elements
● Loop through all the rows of the matrix
● Get the maximum element in the current row and its column
● Set a flag to check whether the max row element is min in column
● Loop through the columns of the matrix
● Check if the maximum element in the current row is the minimum element in the whole column
● If not minimum, then set the flag to false and break out of loop else append that element in the list of valid elements
● Return the valid elements list
"""
def max_row_min_column(matrix: list) -> list:
    max_row_min_col = []
    len_matrix = len(matrix)
    # Iterate over each row in the matrix
    for i in range(len_matrix):
        # Obtain the maximum number in the row and its index
        max_row_num = max(matrix[i])
        index_of_max_row_num = matrix[i].index(max_row_num)
        # Check if the maximum element in the row is also the minimum element in its column
        is_min_in_column = True
        for j in range(len_matrix):
            if matrix[j][index_of_max_row_num] < max_row_num:
                is_min_in_column = False
                break
        if is_min_in_column:
            max_row_min_col.append(max_row_num)
    return max_row_min_col
#Test with [[5,16,20],[9,11,18],[15,16,17]]->17
print(max_row_min_column(matrix=[[5,16,20],[9,11,18],[15,16,17]]))
#Test with [[100,60,20, 50],[70,80,10,90],[10,50,44,30]]->50
print(max_row_min_column(matrix=[[100,60,20, 50],[70,80,10,90],[10,50,44,30]]))
"""c) TESTS"""
#Test for none of the elements matrix[i][j] qualifying the conditions of max row, min column
#Test matrix = [[85,86,87,88],[84,81,78,75],[83,80,77,74],[73,79,76,82]]->[]
print(max_row_min_column(matrix=[[85,86,87,88],[84,81,78,75],[83,80,77,74],[73,79,76,82]]))

# b) SPACE & TIME COMPLEXITY
"""
● The space complexity of the algorithm is 0(1) since I did not create any new matrix during the iterations
● The time complexity is derived as follows (assuming the length of rows is m, columns is n):
1. The outer for loop for the rows goes through the whole array hence it is 0(m)
2. The max function has time complexity of 0(n) and it is called for every length of the row,m => 0(m)
3. The inner for loop for the colum goes through the array n times,length of the column => 0(n) 
4. Assuming all the matrices passed are square matrices, then m==n
Hence the time complexity will be 0(n^3) worst case
● It is not possible to make this array more efficient than this as the algorithm must examine every element at least once
to determine which elements are maximum in their row and minimum in their columns.
● The improvements that I could make on this algorithm are:
-> Computing the maximum elements in each row beforehand and storing them separately so as to reduce the number of times I call max() function
"""
