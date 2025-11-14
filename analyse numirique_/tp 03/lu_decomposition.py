import numpy as np

def print_system(A, b):
    n = len(A)
    for i in range(n):
        row = [f"{A[i,j]:6.4f}" for j in range(n)]
        print(f"[ {' '.join(row)} : {b[i]:6.4f} ]")


def lu_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        L[i][i] = 1

        for j in range(i, n):
            U[i][j] = A[i][j]
            for k in range(i):
                U[i][j] -= L[i][k] * U[k][j]

        for j in range(i + 1, n):
            L[j][i] = A[j][i]
            for k in range(i):
                L[j][i] -= L[j][k] * U[k][i]
            L[j][i] /= U[i][i]

    return L, U

def forward_substitution(L, b):
    n = len(b)
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i][j] * y[j]
    return y

def backward_substitution(U, y):
    n = len(y)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = y[i]
        for j in range(i + 1, n):
            x[i] -= U[i][j] * x[j]
        x[i] /= U[i][i]
    return x

def solve_linear_system_lu(A, b):
    print("* Le systeme initial est :")
    print_system(A, b)

    try:
        L, U = lu_decomposition(A)

        print("\n-------- Décomposition LU --------")
        print("\n* Matrice L :")
        print_system(L, np.zeros(len(b)))
        print("\n* Matrice U :")
        print_system(U, np.zeros(len(b)))

        y = forward_substitution(L, b)
        print("\n* Résolution de Ly = b (descente) :")
        for i, val in enumerate(y):
            print(f"y_{i+1} = {val:.6f}")

        x = backward_substitution(U, y)
        print("\n* Résolution de Ux = y (remontée) :")
        for i, val in enumerate(x):
            print(f"x_{i+1} = {val:.6f}")

        return x

    except ValueError as e:
        print(f"Error solving system: {e}")
        return None

