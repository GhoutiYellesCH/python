import numpy as np
from gauss import solve_linear_system as gauss_solve
from gauss_partial_pivot import solve_linear_system_partial_pivot
from gauss_total_pivot import solve_linear_system_gauss_jordan
from lu_decomposition import solve_linear_system_lu

def input_matrix():
    N = int(input("How big is your matrix N*N: "))
    A = np.zeros((N,N), dtype=float)
    b = np.zeros(N, dtype=float)

    print("Enter elements for matrix A:")
    for i in range(N):
        for j in range(N):
            A[i][j] = float(input(f"Enter element {i+1},{j+1} in A: "))

    print("Enter elements for vector b:")
    for i in range(N):
        b[i] = float(input(f"Enter element {i+1} in b: "))

    return A, b

def print_system(A, b):
    n = len(A)
    for i in range(n):
        row = [f"{A[i,j]:6.4f}" for j in range(n)]
        print(f"[ {' '.join(row)} : {b[i]:6.4f} ]")


def choose_method(method):
    print(f"\n{method} Method:")
    print("1. Iterative")
    print("2. Recursive")
    choice = input("Choose method (1-2): ")
    return choice

def main_menu():
    A, b = None, None
    while True:
        print("\n--- Linear System Solver Menu ---")
        print("1. Read System")
        print("2. Show System")
        print("3. Direct Methods")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            A, b = input_matrix()
        elif choice == '2':
            if A is not None and b is not None:
                print("\nCurrent System:")
                print_system(A, b)
            else:
                print("No system has been input yet.")
        elif choice == '3':
            if A is None or b is None:
                print("Please input a system first.")
                continue

            print("\nDirect Methods:")
            print("a. Gaussian Elimination (with non-null pivot)")
            print("b. Gaussian Elimination (with partial pivoting)")
            print("c. Gaussian Elimination (with total pivoting)")
            print("d. LU Decomposition")

            method_choice = input("Choose a method (a-d): ")

            solution = None
            if method_choice == 'a':
                if choose_method("Gaussian Elimination with non null pivot") == '1':
                    solution = gauss_solve(A, b, 1)
                else:
                    solution = gauss_solve(A, b, 0)
            elif method_choice == 'b':
                if choose_method("Gaussian Elimination with partiel pivoting") == '1':
                    solution = solve_linear_system_partial_pivot(A, b, 1)
                else:
                    solution = solve_linear_system_partial_pivot(A, b, 0)
            elif method_choice == 'c':
                if choose_method("Gaussian Elimination with total pivoting") == '1':
                    solution = solve_linear_system_gauss_jordan(A, b,1)
                else:
                    solution = solve_linear_system_gauss_jordan(A, b,0)
            elif method_choice == 'd':
                if choose_method("LU Decomposition") == '1':
                    solution = solve_linear_system_lu(A, b)
            else:
                print("Invalid choice.")
                continue

            if solution is not None:
                print("\nFinal Solution:")
                for i, val in enumerate(solution):
                    print(f"x_{i+1} = {val:.6f}")
            else:
                print("Failed to solve the system. The matrix may be singular.")
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

