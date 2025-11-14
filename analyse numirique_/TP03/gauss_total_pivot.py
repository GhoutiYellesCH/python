import numpy as np

def print_system(A, b):
    n = len(A)
    for i in range(n):
        row = [f"{A[i,j]:6.4f}" for j in range(n)]
        print(f"[ {' '.join(row)} : {b[i]:6.4f} ]")


def gauss_jordan_elimination_total_pivot(A, b):
    n = len(A)
    A = A.copy().astype(float)
    b = b.copy().astype(float)
    
    print("* Le systeme initial est :")
    print_system(A, b)
    
    for k in range(n):
        max_element = 0
        max_row = k
        max_col = k
        for i in range(k, n):
            for j in range(k, n):
                if abs(A[i, j]) > max_element:
                    max_element = abs(A[i, j])
                    max_row = i
                    max_col = j
        
        if max_row != k:
            A[[k, max_row]] = A[[max_row, k]]
            b[k], b[max_row] = b[max_row], b[k]
        if max_col != k:
            A[:, [k, max_col]] = A[:, [max_col, k]]
        
        print(f"\n* Iteration K= {k+1} :")
        
        if abs(A[k, k]) < 1e-10:
            raise ValueError("Matrix is singular or nearly singular")
        
        # Make the pivot element 1
        pivot = A[k, k]
        A[k] = A[k] / pivot
        b[k] = b[k] / pivot
        
        # Eliminate the variable from all other equations
        for i in range(n):
            if i != k:
                factor = A[i, k]
                A[i] = A[i] - factor * A[k]
                b[i] = b[i] - factor * b[k]
        
        print_system(A, b)
    
    return A, b

def find_max_element(A, k, n):
    submatrix = A[k:n, k:n]
    max_index = np.unravel_index(np.argmax(np.abs(submatrix)), submatrix.shape)
    return k + max_index[0], k + max_index[1]

def eliminate_variable(A, b, k, n):
    if k == n:
        return A, b
    
    factor = A[:, k] / A[k, k]
    factor[k] = 0  
    A -= np.outer(factor, A[k])
    b -= factor * b[k]
    
    return eliminate_variable(A, b, k + 1, n)

def gauss_jordan_elimination_total_pivot_rec(A, b, k=0):
    n = len(A)
    
    if k == 0:
        A = A.copy().astype(float)
        b = b.copy().astype(float)
        print("* Le systeme initial est :")
        print_system(A, b)
    
    if k == n:
        return A, b
    
    max_row, max_col = find_max_element(A, k, n)
    
    if max_row != k:
        A[[k, max_row]] = A[[max_row, k]]
        b[k], b[max_row] = b[max_row], b[k]
    if max_col != k:
        A[:, [k, max_col]] = A[:, [max_col, k]]
    
    print(f"\n* Iteration K= {k+1} :")
    
    pivot = A[k, k]
    A[k] /= pivot
    b[k] /= pivot
    
    A, b = eliminate_variable(A, b, k, n)
    
    print_system(A, b)
    
    return gauss_jordan_elimination_total_pivot_rec(A, b, k + 1)



def solve_linear_system_gauss_jordan(A, b,i):
    try:
        if i == 1:
            A_reduced, b_solution = gauss_jordan_elimination_total_pivot(A, b)
        else:
            A_reduced, b_solution = gauss_jordan_elimination_total_pivot_rec(A, b)
            print(A_reduced, b_solution)
            
        print("\n-------- Gauss-Jordan avec pivot total --------")
        print("\n* La matrice reduite :")
        print_system(A_reduced, b_solution)
        
        print("\n* La resolution donne :")
        for i, val in enumerate(b_solution):
            print(f"x_{i+1} = {val:.6f} ;")
        
        return b_solution
    
    except ValueError as e:
        print(f"Error solving system: {e}")
        return None

