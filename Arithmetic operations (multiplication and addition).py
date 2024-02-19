def get_matrix_from_user(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Enter element at position ({i+1},{j+1}): "))
            row.append(element)
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(row)

def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = [sum(pair) for pair in zip(matrix1[i], matrix2[i])]
        result.append(row)
    return result

def multiply_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            element = sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2)))
            row.append(element)
        result.append(row)
    return result