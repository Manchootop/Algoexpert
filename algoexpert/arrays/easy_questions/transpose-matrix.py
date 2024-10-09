def transposeMatrix(matrix):
    return list(zip(*matrix))


def transposeMatrix2(matrix):
    if not matrix:
        return []

    num_rows = len(matrix)
    num_cols = len(matrix[0])
    new_matrix = [[0] * num_rows for _ in range(num_cols)]
    for i in range(num_rows):
        for j in range(num_cols):
            new_matrix[j][i] = matrix[i][j]

    return new_matrix


print(transposeMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(transposeMatrix2([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))