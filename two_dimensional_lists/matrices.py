import random

def generate_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            value = random.randint(-10, 10) # Здесь можно настроить диапазон случайных значений
            row.append(value)
        matrix.append(row)
    return matrix

def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = matrix1[i][j] + matrix2[i][j]
            row.append(value)
        result.append(row)
    return result

rows = int(input("Введите количество строк матриц: "))
cols = int(input("Введите количество столбцов матриц: "))

matrix1 = generate_matrix(rows, cols)

matrix2 = generate_matrix(rows, cols)

print("Первая матрица:")
for row in matrix1:
    print(row)
print("Вторая матрица:")
for row in matrix2:
    print(row)

result_matrix = add_matrices(matrix1, matrix2)
print("Результат сложения:")
for row in result_matrix:
    print(row)