'''Написати програму розв’язування систем 3 лінійних рівнянь з 3 невідомими, та вказати
розв’язок X системи AX= B, де A – матриця коефіцієнтів, B – вектор вільних членів, X – вектор '''



def Ai(A, B, i) -> list:
    """Повертає матрицю А з заміненим i-им стовпчиком на вектор B"""
    Ai = [[],[],[]]
    for j in range(3):
        for k in range(3):
            if k == i:
                Ai[j].append(B[j])
            else:
                Ai[j].append(A[j][k])
    return Ai

def det(matrix) -> int:
    """Рахує визначник матриці 3х3"""
    ''' Метод трикутника '''
    return (matrix[0][0] * matrix[1][1] * matrix[2][2]) + \
           (matrix[0][1] * matrix[1][2] * matrix[2][0]) + \
           (matrix[0][2] * matrix[1][0] * matrix[2][1]) - \
           (matrix[0][2] * matrix[1][1] * matrix[2][0]) - \
           (matrix[0][0] * matrix[1][2] * matrix[2][1]) - \
           (matrix[0][1] * matrix[1][0] * matrix[2][2])

def solveKramer(A, B) -> list:
    """Розв'язує систему рівнянь методом Крамера"""
    detA = det(A)
    if detA == 0:
        return None
    X = []
    for i in range(3):
        detAi = det(Ai(A, B, i))
        X.append(detAi / detA)
    return X

if __name__ == "__main__":
    A = [[],[],[]]
    B = []
    
    print("Введіть матрицю А: ")
    for i in range(3):
        for j in range(3):
            print(f"A[{i}][{j}] = ", end="")
            A[i].append(int(input()))

    print("Введіть матрицю B: ")
    for i in range(3):
        print(f"B[{i}] = ", end="")
        B.append(int(input()))

    X = solveKramer(A, B)
    if X is None:
        print("Система не має розв'язків")
    else:
        result = "X^T = (" + " ".join(str(int(X[i])) for i in range(3)) + ")"
        print(result)

# answer is 0, -1, 1