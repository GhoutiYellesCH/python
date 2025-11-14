import numpy as np

def jacobi_iterative(A, b, x0, maxIteration):
    n = len(A)
    x = np.array(x0, dtype=float)
    print("Initial guess:", x)
    iteration = 0
    
    while True:
        x_new = np.zeros_like(x)
        for i in range(n):
            sum_except_i = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_except_i) / A[i][i]
        
        iteration += 1
        print(f"Iteration {iteration}: x = {x_new}")
        
        if iteration >= maxIteration: # Reached maximum iterations
            return x_new, iteration  # Converged solution and iteration count
        x = x_new


def jacobi_recursive(A, b, x, maxIterations, i=0, j=0, iteration=0, x_new=None):
    n = len(A)
    
    if x_new is None:
        x_new = np.zeros_like(x)
    
    if i < n:
        if j < n:
            if i != j:
                x_new[i] -= A[i][j] * x[j]
            return jacobi_recursive(A, b, x, maxIterations, i, j+1, iteration, x_new)
        else:
            x_new[i] = (b[i] + x_new[i]) / A[i][i]
            return jacobi_recursive(A, b, x, maxIterations, i+1, 0, iteration, x_new)
    else:
        print(f"Iteration {iteration+1}: x = {x_new}")
        
        if iteration >= maxIterations - 1 :
            return x_new, iteration + 1
        
        return jacobi_recursive(A, b, x_new, maxIterations, 0, 0, iteration + 1)


def solve_linear_system(A, b, x0, method_flag, maxIterations=15):
    print("\n" + "-" * 20 + f" Jacobi {'Iterative' if method_flag == 1 else 'Recursive'} " + "-" * 20)

    if method_flag == 1:
        solution, iterations = jacobi_iterative(A, b, x0, maxIterations)
    else:
        solution, iterations = jacobi_recursive(A, b, np.array(x0, dtype=float), maxIterations)

    print("\nSolution:")
    for i, val in enumerate(solution):
        print(f"x_{i+1} = {val:.6f}")
    return solution



def print_system(A, b):
    n = len(A)
    print("System:")
    for i in range(n):
        row = [f"{A[i,j]:6.4f}" for j in range(n)]
        print(f"[ {' '.join(row)} : {b[i]:6.4f} ]")

if __name__ == "__main__":
    A = np.array([[10, 1, 1],
                  [1, 10, 1],
                  [1, 1, 10],])
    b = np.array([6, 12, 3])
    x0 = [0, 0, 0]

    print_system(A, b)
    
solve_linear_system(A,b, x0, 1)

    