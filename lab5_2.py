import numpy as np

# Створюємо пустий масив 7x7
matrix = np.zeros((7, 7), dtype=int)

# Заповнюємо масив
for i in range(7):
    for j in range(i+1, 7):
        matrix[i][j] = 1
        matrix[6-i][j] = 1

# Виводимо масив на екран
for row in matrix:
    print(' '.join(map(str, row)))
