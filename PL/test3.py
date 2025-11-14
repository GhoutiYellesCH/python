def saisir_matrice():
    """Saisit la matrice initiale du tableau du simplexe à partir de l'utilisateur."""
    matrice = []
    while True:
        row = input("Enter a row of values separated by spaces (or 'q' to quit): ").strip()
        if row.lower() == 'q':
            break
        row_values = [float(x) for x in row.split()]
        matrice.append(row_values)
    return matrice

def saisir_matrice1():
    """Saisit la matrice initiale du tableau du simplexe à partir de l'utilisateur."""
    matrice = []
    while True:
        row = input("Enter a row of values separated by spaces (or 'q' to quit): ").strip()
        if row.lower() == 'q':
            break
        row_values = [float(x) for x in row.split()]
        matrice.append(row_values)
    return matrice


def chercher_variable_entrante(matrice):
    """Cherche la variable entrante (colonne avec le plus grand Cj-Zj positif)."""
    max_cj_zj = 0
    col = -1
    for j in range(len(matrice[0]) - 1):
        if matrice[0][-1][j] > max_cj_zj:
            max_cj_zj = matrice[0][-1][j]
            col = j
    return col

def chercher_variable_sortante(matrice, col_entrante):
    """Cherche la variable sortante (ligne avec le plus petit ratio non négatif)."""
    min_ratio = float('inf')
    row = -1
    for i in range(1, len(matrice) - 1):
        if matrice[i][col_entrante] > 0:
            ratio = matrice[i][-1] / matrice[i][col_entrante]
            if ratio < min_ratio:
                min_ratio = ratio
                row = i
    return row

def pivoter(matrice, pivot_row, pivot_col):
    """Effectue l'opération de pivotage."""
    pivot_value = matrice[pivot_row][pivot_col]
    for j in range(len(matrice[0])):
        matrice[pivot_row][j] /= pivot_value
    for i in range(len(matrice)):
        if i != pivot_row:
            factor = matrice[i][pivot_col]
            for j in range(len(matrice[0])):
                matrice[i][j] -= factor * matrice[pivot_row][j]
    return matrice

def afficher_matrice(matrice):
  for row in matrice:
    for element in row:
      print(f"{element:8.2f}", end=" ")  # Format each element with 8 characters and 2 decimal places
    print()

def est_optimale(matrice):
    """Vérifie si la solution est optimale."""
    for j in range(len(matrice[0]) - 1):
        if matrice[0][-1][j] > 0:
            return False
    return True

def methode_simplexe(matrice_initiale):
    """Implémentation de la méthode du simplexe."""
    matrice = matrice_initiale.copy()
    while not est_optimale(matrice):
        col_entrante = chercher_variable_entrante(matrice)
        row_sortante = chercher_variable_sortante(matrice, col_entrante)
        pivoter(matrice, row_sortante, col_entrante)
    return matrice

# Example usage:
matrice_initiale = saisir_matrice()
solution_optimale = methode_simplexe(matrice_initiale)
afficher_matrice(solution_optimale)  