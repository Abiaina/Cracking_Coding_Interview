def forward_rotate (matrix):
    # Rotates square matrix by +90 degrees in place.
    # Time: O(n^2)

    axis = 0
    # Time: O(n^2)
    for r_i, row in enumerate(matrix):
        for c_i, col in enumerate(matrix):
            if c_i > axis:
                # Transpose column and row:
                tmp_top = matrix[c_i][r_i]
                matrix[c_i][r_i] = matrix[r_i][c_i]
                matrix[r_i][c_i] = tmp_top
        axis += 1

    # Reverse columns in each row.
    # Time: O(n^2)
    for r_i, row in enumerate(matrix):
        # Time: O(n)
        # Space: O(1)
        row.reverse()  
    return matrix



# Tests
test1_matrix = [[1,2,3],[4,5,6],[7,8,9]]
test2_matrix = [[ 5, 1, 9,11], [ 2, 4, 8,10], [13, 3, 6, 7], [15,14,12,16]]
test_1 = [[7,4,1], [8,5,2],[9,6,3]] == forward_rotate(test1_matrix)
test_2 = [[15,13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7,10,11]] == forward_rotate(test2_matrix)
if test_1:
    print("Print Test 1 Passed!")
else:
    print("Print Test 1 Failed !")
if test_2:
    print("Print Test 2 Passed!")
else:
    print("Print Test 2 Failed !")