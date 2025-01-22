# Your code here
def matrix_builder(number):
    matrix = []

    for i in range(number):
        row = []
        for j in range(number):
            row.append(1)
        matrix.append(row)
    return matrix

print(matrix_builder(3))