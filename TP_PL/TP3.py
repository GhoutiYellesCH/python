import numpy as np

def input_initial_matrix():
    c = list(map(float, input("Enter the coefficients of the objective function (c1, c2, ..., cn): ").split()))

    num_constraints = int(input("Enter the number of constraints: "))

    A = []
    b = []
    
    for i in range(num_constraints):
        row = list(map(float, input(f"Enter coefficients for constraint {i + 1} (a1, a2, ..., an): ").split()))
        A.append(row)
        b.append(float(input(f"Enter the right-hand side value for constraint {i + 1}: ")))

    c = np.array(c)
    A = np.array(A)
    b = np.array(b)

    return c, A, b

def display_tableau(tableau):
    print("\nCurrent Tableau:")
    print(" " * 5 + " | " + " | ".join([f"x{i}" for i in range(len(tableau[0]) - 1)]) + " | RHS")
    print("-" * (5 + 4 * (len(tableau[0]) - 1) + 7))
    for i, row in enumerate(tableau):
        print(f"Row {i}: " + " | ".join(f"{val:8.2f}" for val in row))
    print("\n")

def simplex_method(c, A, b):
    num_vars = len(c)
    num_constraints = len(b)

    tableau = np.zeros((num_constraints + 1, num_vars + num_constraints + 1))

    tableau[0, 1:num_vars + 1] = c 
    tableau[1:num_constraints + 1, 0] = range(num_constraints)
    tableau[1:num_constraints + 1, 1:num_vars + 1] = A
    tableau[1:num_constraints + 1, num_vars + 1:num_vars + num_constraints + 1] = np.eye(num_constraints)
    tableau[1:num_constraints + 1, -1] = b
   
    display_tableau(tableau)

    while True:
        if all(tableau[0, 1:-1] >= 0):
            break

        entering = np.argmin(tableau[0, 1:-1]) + 1
        ratios = tableau[1:, -1] / tableau[1:, entering]
        ratios[ratios <= 0] = np.inf
        leaving = np.argmin(ratios) + 1

        pivot = tableau[leaving, entering]
        tableau[leaving] /= pivot

        for i in range(tableau.shape[0]):
            if i != leaving:
                tableau[i] -= tableau[leaving] * tableau[i, entering]

        display_tableau(tableau)

    solution = np.zeros(num_vars)
    for i in range(1, num_constraints + 1):
        if tableau[i, 0] < num_vars:
            solution[int(tableau[i, 0])] = tableau[i, -1]

    objective_value = tableau[0, -1]

    return solution, objective_value

def determine_solution_type(solution, objective_value):
    if np.any(solution < 0):
        return "Infeasible"
    else:
        return f"Optimal solution found with objective value: {objective_value:.2f}"

if __name__ == "__main__":
    c, A, b = input_initial_matrix()
    solution, objective_value = simplex_method(c, A, b)
    solution_type = determine_solution_type(solution, objective_value)

    print("\nFinal Solution:")
    for i, val in enumerate(solution):
        print(f"x{i + 1} = {val:.2f}")
    print(solution_type)
