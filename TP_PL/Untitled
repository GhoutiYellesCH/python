import numpy as np

def input_initial_matrix():
    """
    Function to input the initial matrix for the Simplex method.
    The user will input the coefficients of the objective function and constraints.
    """
    # Input the coefficients of the objective function
    c = list(map(float, input("Enter the coefficients of the objective function (c1, c2): ").split()))
    
    # Input the number of constraints
    num_constraints = int(input("Enter the number of constraints: "))
    
    # Initialize the matrix
    A = []
    b = []
    
    for i in range(num_constraints):
        row = list(map(float, input(f"Enter coefficients for constraint {i + 1} (a1, a2, ..., an): ").split()))
        A.append(row)
        b.append(float(input(f"Enter the right-hand side value for constraint {i + 1}: ")))
    
    # Convert to numpy arrays
    c = np.array(c)
    A = np.array(A)
    b = np.array(b)
    
    return c, A, b

def simplex_method(c, A, b):
    """
    Function to solve the linear programming problem using the Simplex method.
    """
    num_vars = len(c)
    num_constraints = len(b)
    
    # Create the tableau
    tableau = np.zeros((num_constraints + 1, num_vars + num_constraints + 1))
    
    # Fill the tableau with the coefficients
    tableau[0, 1:num_vars + 1] = c
    tableau[1:num_constraints + 1, 0] = range(1, num_constraints + 1)
    tableau[1:num_constraints + 1, 1:num_vars + 1] = A
    tableau[1:num_constraints + 1, num_vars + 1:num_vars + num_constraints + 1] = np.eye(num_constraints)
    tableau[1:num_constraints + 1, -1] = b
    
    # Simplex algorithm
    while True:
        # Check for optimality
        if all(tableau[0, 1:-1] >= 0):
            break
        
        # Determine entering variable
        entering = np.argmin(tableau[0, 1:-1]) + 1
        
        # Determine leaving variable
        ratios = tableau[1:, -1] / tableau[1:, entering]
        ratios[ratios <= 0] = np.inf  # Ignore non-positive ratios
        leaving = np.argmin(ratios) + 1
        
        # Perform pivot
        pivot = tableau[leaving, entering]
        tableau[leaving] /= pivot
        
        for i in range(tableau.shape[0]):
            if i != leaving:
                tableau[i] -= tableau[leaving] * tableau[i, entering]
    
    # Extract the solution
    solution = np.zeros(num_vars)
    for i in range(1, num_constraints + 1):
        if tableau[i, 0] < num_vars:
            solution[int(tableau[i, 0])] = tableau[i, -1]
    
    return solution, tableau[0, -1]

def determine_solution_type(solution, objective_value):
    """
    Function to determine the type of solution.
    """
    if np.any(solution < 0):
        return "Infeasible"
    else:
        return f"Optimal solution found with objective value: {objective_value}"

# Example usage
if __name__ == "__main__":
    c, A, b = input_initial_matrix()
    solution, objective_value = simplex_method(c, A, b)
    solution_type = determine_solution_type(solution, objective_value)
    
    print("Solution:", solution)
    print(solution_type)
