import numpy as np

def forward_substitution(A, b):
    n = len(b)
    x = np.zeros_like(b, dtype=float)
    
    for i in range(n):
        sum = 0
        for j in range(i):  
            sum += A[i, j] * x[j]
        x[i] = (b[i] - sum) / A[i, i]  
    return x

def backward_substitution(A, b):
    n = len(b)
    x = np.zeros_like(b, dtype=float)  
    
    for i in range(n-1, -1, -1):  
        sum_ = 0
        for j in range(i+1, n):  
            sum_ += A[i, j] * x[j]
        x[i] = (b[i] - sum_) / A[i, i]  
    return x

A_lower = np.array([
    [-2, 0, 0],
    [-1, 3, 0],
    [4, 1, 3]
], dtype=float)
b_lower = np.array([4, -1, 0], dtype=float)

x_lower = forward_substitution(A_lower, b_lower)
print("Solution for lower triangular system:", x_lower)

A_upper = np.array([
    [3, 2, 5],
    [0, 1, -3],
    [0, 0, 1]
], dtype=float)
b_upper = np.array([4, -2, 1], dtype=float)

x_upper = backward_substitution(A_upper, b_upper)
print("Solution for upper triangular system:", x_upper)
