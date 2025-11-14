import numpy as np

def print_system(A, b):
    n = len(A)
    for i in range(n):
        row = [f"{A[i,j]:6.4f}" for j in range(n)]
        print(f"[ {' '.join(row)} : {b[i]:6.4f} ]")

def gaussian_elimination_partial_pivot(A, b):
    n = len(A)
    m = len(A[0])
    A = A.copy().astype(float)
    b = b.copy().astype(float)
    
    print("* Le systeme est :")
    print_system(A, b)
    
    for k in range(1, n + 1):
        p = abs(A[k-1, k-1])
        l = k - 1
        
        for i in range(k - 1, n):
            if abs(A[i, k-1]) > p:
                p = abs(A[i, k-1])
                l = i
        
        if l != k - 1:
            for j in range(k - 1, m):
                temp = A[k-1, j]
                A[k-1, j] = A[l, j]
                A[l, j] = temp
            temp = b[k-1]
            b[k-1] = b[l]
            b[l] = temp
        
        print(f"\n* Iteration K= {k} :")
        
        for i in range(k, n):
            q = A[i, k-1] / A[k-1, k-1]
            A[i, k-1] = 0
            for j in range(k, m):
                A[i, j] = A[i, j] - A[k-1, j] * q
            b[i] = b[i] - b[k-1] * q
        
        print_system(A, b)
    
    return A, b

def gaussian_elimination_partial_pivot_recursive(A, b, k=0):
    n = len(A)
    
    if k == 0:
        A = A.copy().astype(float)
        b = b.copy().astype(float)
        print("* Le systeme est :")
        print_system(A, b)
    
    if k == n - 1:
        return A, b
    
    pivot_row = k + np.argmax(np.abs(A[k:, k]))
    pivot_value = A[pivot_row, k]
    
    if pivot_row != k:
        A[[k, pivot_row]] = A[[pivot_row, k]]
        b[k], b[pivot_row] = b[pivot_row], b[k]
    
    print(f"\n* Iteration K= {k+1} :")
    
    factors = A[k+1:, k] / pivot_value
    A[k+1:, k] = 0
    A[k+1:, k+1:] -= np.outer(factors, A[k, k+1:])
    b[k+1:] -= factors * b[k]
    
    print_system(A, b)
    
    return gaussian_elimination_partial_pivot_recursive(A, b, k + 1)


def backward_substitution(A, b):
    n = len(b)
    x = np.zeros_like(b, dtype=float)
    
    for i in range(n-1, -1, -1):
        sum_ = 0
        for j in range(i+1, n):
            sum_ += A[i, j] * x[j]
        x[i] = (b[i] - sum_) / A[i, i]
    
    return x

def solve_linear_system_partial_pivot(A, b, i):
    
    if i == 1:
        A_upper, b_modified = gaussian_elimination_partial_pivot(A, b)
    else: 
        A_upper, b_modified = gaussian_elimination_partial_pivot_recursive(A, b)

    
    print("\n-------- Gauss avec pivot partiel --------")
    print("\n* La matrice reduite :")
    print_system(A_upper, b_modified)
    
    x = backward_substitution(A_upper, b_modified)
    
    print("\n* La resolution donne :")
    for i, val in enumerate(x):
        print(f"x_{i+1} = {val:.6f} ;")
    
    return x