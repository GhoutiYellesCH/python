import numpy as np

def triangularize(A, b):
    n = len(A)
    A = A.astype(float)
    b = b.astype(float)
    
    print("Initial system:")
    print_system(A, b)
    
    for k in range(n-1):
        pivot = A[k,k]
        if pivot == 0:
            return None, None
            
        print(f"\nItération k = {k+1}:")
        
        for i in range(k+1, n):
            q = A[i,k]
            A[i,k] = 0
            b[i] = b[i] - (q/pivot)*b[k]
            
            for j in range(k+1, n):
                A[i,j] = A[i,j] - (q/pivot)*A[k,j]
        
        print_system(A, b)
                
    return A, b

def triangularizeRec(A, b, k=0, i=None):
    n = len(A)

    if k == 0:
        A = A.astype(float)
        b = b.astype(float)
        print("Initial system:")
        print_system(A, b)

    if k == n-1:
        return A, b

    pivot = A[k,k]
    if pivot == 0:
        return None, None

    if i is None:
        print(f"\nItération k = {k+1}:")
        i = k + 1

    if i < n:
        q = A[i,k]
        A[i,k] = 0
        b[i] = b[i] - (q/pivot)*b[k]

        A[i,k+1:] = A[i,k+1:] - (q/pivot)*A[k,k+1:]

        return triangularizeRec(A, b, k, i+1)
    else:
        print_system(A, b)
        return triangularizeRec(A, b, k+1)


def back_substitute(A, b):
    n = len(A)
    x = np.zeros(n)
    
    for i in range(n-1, -1, -1):
        sum_val = 0
        for k in range(i+1, n):
            sum_val += A[i,k] * x[k]
        x[i] = (b[i] - sum_val) / A[i,i]
        
    return x

def solve_linear_system(A, b, flag):
    print("\n" + "-" * 20 + " Gauss " + "-" * 20)
    
    if flag == 1:
        triang_A, mod_b = triangularize(A, b) 
    else:
        triang_A, mod_b = triangularizeRec(A, b)
        
    if triang_A is None:
        return None
    
    print("\nLa matrice résulte:")
    print_system(triang_A, mod_b)
    
    x = back_substitute(triang_A, mod_b)
    
    print("\nLa résolution donne:")
    for i, val in enumerate(x):
        print(f"x_{i+1} = {val:.6f}")
    
    return x

def print_system(A, b):
    n = len(A)
    for i in range(n):
        row = [f"{A[i,j]:6.4f}" for j in range(n)]
        print(f"[ {' '.join(row)} : {b[i]:6.4f} ]")


