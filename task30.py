#todo: Найти сумму элементов матрицы,
#Написать msum(matrix)  которая подсчитывает сумму всех элементов функцию Найти сумму всех элементов матрицы:
#>>> matrix = [[1, 2, 3], [4, 5, 6]]
#>>> msum(matrix)
#21
#>>> msum(load_matrix('matrix.txt'))
#423
import numpy as np
def msum(matrix):
    s = np.sum(matrix)
    return s
print(msum([[1, 2, 3], [4, 5, 6]]))

def msum(load_matrix):
    with open('matrix.txt.TXT') as f:
        matrix = [list(map(int, row.split())) for row in f.readlines()]
        return np.sum(matrix)
print(msum('matrix.txt.TXT'))
