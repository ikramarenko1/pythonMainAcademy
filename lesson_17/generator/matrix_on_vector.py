# Множення матриці на вектор: Реалізуйте генератор для обчислення добутку матриці на вектор.
def matrix_vector(matrix, vector):
    for row in matrix:
        yield sum(a * b for a, b in zip(row, vector))


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
vector = [1, 0, 1]

matrix_vector_generator = matrix_vector(matrix, vector)
result = [result for result in matrix_vector_generator]

print(result)
