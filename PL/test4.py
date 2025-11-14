import numpy as np

def chercher_variable_entrante(tableau):
    """
    Finds the entering variable in a simplex tableau.

    Args:
        tableau: A 2D NumPy array representing the simplex tableau.

    Returns:
        The index of the entering variable.
    """

    # Find the index of the most negative coefficient in the objective row
    return np.argmin(tableau[0, :-1])

def chercher_variable_sortante(tableau, col_entrante):
    """
    Finds the leaving variable in a simplex tableau.

    Args:
        tableau: A 2D NumPy array representing the simplex tableau.
        col_entrante: The index of the entering variable.

    Returns:
        The index of the leaving variable.
    """

    min_ratio = float('inf')
    min_index = -1
    for i in range(1, len(tableau)):
        if tableau[i, col_entrante] > 0:
            ratio = tableau[i, -1] / tableau[i, col_entrante]
            if ratio < min_ratio:
                min_ratio = ratio
                min_index = i
    return min_index

def pivoter(tableau, ligne_pivot, colonne_pivot):
    """
    Performs the pivot operation on a simplex tableau.

    Args:
        tableau: A 2D NumPy array representing the simplex tableau.
        ligne_pivot: The index of the pivot row.
        colonne_pivot: The index of the pivot column.

    Returns:
        The updated simplex tableau.
    """

    pivot_value = tableau[ligne_pivot, colonne_pivot]
    tableau[ligne_pivot] /= pivot_value
    for i in range(len(tableau)):
        if i != ligne_pivot:
            factor = tableau[i, colonne_pivot]
            tableau[i] -= factor * tableau[ligne_pivot]
    return tableau

def est_optimale(tableau):
    """
    Checks if the current solution is optimal.

    Args:
        tableau: A 2D NumPy array representing the simplex tableau.

    Returns:
        True if the solution is optimal, False otherwise.
    """

    return np.all(tableau[0, :-1] >= 0)

def methode_simplexe(tableau_initial):
    tableau = tableau_initial.copy()
    while not est_optimale(tableau):
        col_entrante = chercher_variable_entrante(tableau)
        ligne_sortante = chercher_variable_sortante(tableau, col_entrante)
        pivoter(tableau, ligne_sortante, col_entrante)
    return tableau

# Example usage:
tableau_initial = np.array([[2, 1, 1, 0, 0, 400],
                           [1, 0, 0, 1, 0, 150],
                           [0, 1, 0, 0, 1, 200],
                           [-800, -300, 0, 0, 0, 0]])

solution_optimale = methode_simplexe(tableau_initial)
print(solution_optimale)