import numpy as np

def gauss_seidel_iterative(A, b, x0, max_iterations=100):
    
    n = len(A)
    x = np.array(x0, dtype=float)
    print("Initial guess:", x)
    
    for iteration in range(max_iterations):
        x_new = np.copy(x)
        for i in range(n):
            sum1 = sum(A[i][j] * x_new[j] for j in range(i))  # Already updated values
            sum2 = sum(A[i][j] * x[j] for j in range(i+1, n))  # Previous values
            x_new[i] = (b[i] - sum1 - sum2) / A[i][i]
        
        print(f"Iteration {iteration+1}: x = {x_new}")
        x = x_new  

    return x, max_iterations


def gauss_seidel_recursive(A, b, x, max_iterations=100, iteration=0, i=0):
    n = len(A)
    
    if iteration == 0 and i == 0:
        x_new = np.copy(x)
    else:
        x_new = x

    if i < n:
        sum1 = np.sum(A[i][:i] * x_new[:i])
        sum2 = np.sum(A[i][i+1:] * x[i+1:])
        x_new[i] = (b[i] - sum1 - sum2) / A[i][i]
        return gauss_seidel_recursive(A, b, x_new, max_iterations, iteration, i + 1)
    else:
        print(f"Iteration {iteration+1}: x = {x_new}")
        
        if iteration >= max_iterations - 1:
            return x_new, max_iterations
        
        return gauss_seidel_recursive(A, b, x_new, max_iterations, iteration + 1, 0)

def solve_linear_system(A, b, x0, method_flag, max_iterations):
    print("\n" + "-" * 20 + f" Gauss-Seidel {'Iterative' if method_flag == 1 else 'Recursive'} " + "-" * 20)
    
    if method_flag == 1:
        solution, iterations = gauss_seidel_iterative(A, b, x0, max_iterations)
    else:
        solution, iterations = gauss_seidel_recursive(A, b, np.array(x0, dtype=float), max_iterations)
    
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


# Example usage
if __name__ == "__main__":
    A = np.array([[4, 1, -1],
                  [2, 7, 1],
                  [1,-3, 12]])
    b = np.array([3, 19, 31])
    x0 = [0, 0, 0]
    max_iterations = 10

    print_system(A, b)

    solve_linear_system(A, b, x0, method_flag=1, max_iterations=max_iterations)

    solve_linear_system(A, b, x0, method_flag=0, max_iterations=max_iterations)
