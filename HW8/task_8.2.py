# Задача 2. Дана квадратная матрица, заполненная случайными числами.
# Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.

import random as r

def Sum_Diagonl(size):
    sum_d = 0
    for i in range(size):
            print(matrix[i][i], end= ' ')
            sum_d += matrix[i][i]
    return sum_d

def Sum_Row(matrix):
    sum_r = []
    for i in matrix:
        sum_r.append(sum(i))
    return sum_r

def Withdraw_Matrix(matrix):
    print("Исходная матрица")
    for i in matrix:
        print(i)

size = int(input("введите размер квадратной матрицы: "))
matrix=[0]*size

for i in range(size):
    matrix[i] = list(r.randint(1,10) for j in range(size))
Withdraw_Matrix(matrix)

sum_diagonal = Sum_Diagonl(size)
sun_line = Sum_Row(matrix)

for i in range(len(sun_line)):
    if sun_line[i]> sum_diagonal:
        print(f'В строке {i+1} сумма элементов больше чем сумма элементов диагонали')

