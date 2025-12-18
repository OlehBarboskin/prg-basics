matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

def change_matrix(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            matrix [0][0] = 1
            matrix [1][1] = 1
            matrix [2][2] = 1
        return matrix

print(change_matrix(matrix))