import numpy as np

def max_row_min_column(matrix):
    # Convert the input to a NumPy array for ease of use
    mat = np.array(matrix)
    
    # Get the dimensions of the matrix
    num_rows, num_cols = mat.shape
    
    # Initialize an empty list to store the results
    results = []
    
    # Iterate over each row in the matrix
    for i in range(num_rows):
        # Find the maximum element in the current row
        max_in_row = max(mat[i])
        
        # Find the index of the maximum element in the current row
        max_index = np.where(mat[i] == max_in_row)[0][0]
        
        # Check if the maximum element in the row is also the minimum in its column
        is_min_in_col = all(mat[j][max_index] >= max_in_row for j in range(num_rows))
        
        # If so, add the element to the results list
        if is_min_in_col:
            results.append(max_in_row)
    
    # Return the list of results
    return results


print(max_row_min_column(matrix=[[85,86,87,88,100],[84,81,78,75],[83,80,77,74],[73,79,76,82]]))
