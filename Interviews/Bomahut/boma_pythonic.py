def max_row_min_col(mat):
    # Initialize an empty list to store the results
    results = []
    # Iterate over each row in the matrix
    for i in range(len(mat)):
        # Find the maximum element in the current row
        max_in_row = max(mat[i])
        # Find the index of the maximum element in the current row
        max_index = mat[i].index(max_in_row)
        # Check if the maximum element in the row is also the minimum in its column
        if all(mat[j][max_index] >= max_in_row for j in range(len(mat))):
            # If so, add the element to the results list
            results.append(max_in_row)
    # Return the list of results
    return results
#Test with [[5,16,20],[9,11,18],[15,16,17]]->17
print(max_row_min_col(mat=[[5,16,20],[9,11,18],[15,16,17]]))
#Test with [[100,60,20, 50],[70,80,10,90],[10,50,44,30]]->50
print(max_row_min_col(mat=[[100,60,20, 50],[70,80,10,90],[10,50,44,30]]))
"""c) TESTS"""
#Test for none of the elements mat[i][j] qualifying the conditions of max row, min column
#Test mat = [[85,86,87,88],[84,81,78,75],[83,80,77,74],[73,79,76,82]]->[]
print(max_row_min_col(mat=[[85,86,87,88],[84,81,78,75],[83,80,77,74],[73,79,76,82]]))
