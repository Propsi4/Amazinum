'''Написати програму розв’язування систем 3 лінійних рівнянь з 3 невідомими, та вказати
розв’язок X системи AX= B, де A – матриця коефіцієнтів, B – вектор вільних членів, X – вектор '''

import numpy as np


#init matrix A and B
A = np.zeros((3, 3))
B = np.zeros(3)

#input matrix A
print("Введіть матрицю А: ")
for i in range(3):
    for j in range(3):
        print(f"A[{i}][{j}] = ", end="")
        A[i][j] = int(input())

#input matrix B
print("Введіть матрицю B: ")
for i in range(3):
    print(f"B[{i}] = ", end="")
    B[i] = int(input())

#solve system AX = B
X = np.linalg.solve(A, B)

#print result
print("Розв'язок системи: ")
result = "X^T = (" + " ".join(str(X[i]) for i in range(3)) + ")"
print(result)
