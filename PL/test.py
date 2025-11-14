import numpy as np

def simplex(tableau, c):
    """
    Implements the simplex method for linear programming.

    Args:
        tableau: A NumPy array representing the initial tableau.
        c: A NumPy array representing the coefficients of the objective function.

    Returns:
        The optimal solution, if found.
    """

    while True:
        # Find entering variable
        entering_var = np.argmin(c[:-1])

        # Find leaving variable
        ratios = tableau[1:, -1] / tableau[1:, entering_var]
        ratios[tableau[1:, entering_var] <= 0] = np.inf
        leaving_var = np.argmin(ratios) + 1

        # Check for unboundedness
        if np.all(ratios == np.inf):
            print("Unbounded solution")
            return

        # Pivot
        pivot = tableau[leaving_var, entering_var]
        tableau[leaving_var] /= pivot
        for i in range(tableau.shape[0]):
            if i != leaving_var:
                tableau[i] -= tableau[i, entering_var] * tableau[leaving_var]

        # Update objective function
        c -= c[entering_var] * tableau[leaving_var]

        # Check for optimality
        if np.all(c[:-1] >= 0):
            break

    return tableau

# Example usage:
tableau = np.array([[1, -2, -1, 0, 0, 0],
                   [1, 1, 1, 1, 0, 0],
                   [2, 1, 2, 0, 1, 0],
                   [1, 1, 1, 0, 0, 1]])

c = np.array([-1, -2, -1, 0, 0, 0])  

solution = simplex(tableau, c)
print(solution)