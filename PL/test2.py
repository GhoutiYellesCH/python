def saisir_matrice():
    matrice = [
        [0, 0, 800, 300, 0, 0, 0],
        [0, 400, 2, 1, 1, 0, 0],
        [0, 150, 1, 0, 0, 1, 0],
        [0, 200, 0, 1, 0, 0, 1],
        [0, 0, 800, 300, 0, 0, 0],
    ]
    return matrice

# def calc_z(mat):
#   for i in range(len(mat -1)):

def calculate_objective_value(tableau):
  objective_row = tableau[-1]
  z = 0
  for i in range(len(objective_row) - 1):
    if objective_row[i] == 0:
      continue  # Skip non-basic variables
    z += objective_row[-1] * objective_row[i]
  return z

def chercher_variable_entrante(matrice):
    min_val = 0
    min_index = -1
    for i in range(len(matrice[0]) - 1):
        if matrice[0][i] < min_val:
            min_val = matrice[0][i]
            min_index = i
    return min_index


def chercher_variable_sortante(matrice, variable_entrante):
    min_ratio = float("inf")
    min_index = -1
    for i in range(1, len(matrice)):
        if matrice[i][variable_entrante] > 0:
            ratio = matrice[i][-1] / matrice[i][variable_entrante]
            if ratio < min_ratio:
                min_ratio = ratio
                min_index = i
    return min_index


def pivoter(matrice, ligne_pivot, colonne_pivot):
    pivot_value = matrice[ligne_pivot][colonne_pivot]
    matrice[ligne_pivot] = [x / pivot_value for x in matrice[ligne_pivot]]
    for i in range(len(matrice)):
        if i != ligne_pivot:
            factor = matrice[i][colonne_pivot]
            matrice[i] = [
                x - factor * y for x, y in zip(matrice[i], matrice[ligne_pivot])
            ]
    return matrice


def est_optimale(matrice):
    for i in range(len(matrice[0]) - 1):
        if matrice[0][i] < 0:
            return False
    return True


def methode_simplexe(matrice_initiale):
    matrice = matrice_initiale.copy()
    #afficher_matrice(matrice)
    while not est_optimale(matrice):
        variable_entrante = chercher_variable_entrante(matrice)
        print(variable_entrante)
        variable_sortante = chercher_variable_sortante(matrice, variable_entrante)
        matrice = pivoter(matrice, variable_sortante, variable_entrante)
    return matrice


def afficher_matrice(matrice):
    for row in matrice:
        for element in row:
            print(f"{element:8.2f}", end=" ")
        print()


matrice_initiale = saisir_matrice()
solution_optimale = methode_simplexe(matrice_initiale)
afficher_matrice(solution_optimale)
print(calculate_objective_value(matrice_initiale))