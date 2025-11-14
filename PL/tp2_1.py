def saisir_matrice(N, M):

    Mat = []
    #for i in range(N):
     #   row = list(map(float, input(f'Saisir la ligne {i} (séparée par des espaces): ').split()))
      #  Mat.append(row)
    Mat = [[0,0,800,300,0,0,0],
       [0,400,2,1,1,0,0],
       [0,150,1,0,0,1,0],
       [0,200,0,1,0,0,1]]
    return Mat

def chercher_variable_entrante(Mat):

    CjZj = [0] * len(Mat[0])
    Zj = [0] * len(Mat[0])
    
    for i in range(1, len(Mat)):
        for j in range(2, len(Mat[0])):  # Commencer à 2 pour ignorer les variables de base
            Zj[j] += Mat[i][0] * Mat[i][j]
    
    for j in range(2, len(Mat[0])):
        CjZj[j] = Mat[0][j] - Zj[j]

    index = CjZj.index(max(CjZj[2:]))  # Ignorer les deux premières colonnes
    return index

def chercher_variable_sortante(Mat, index):
    Ration = []
    for i in range(1, len(Mat)):  
        if Mat[i][index] > 0:
            Ration.append((Mat[i][1] / Mat[i][index], i))  
    if not Ration:
        raise ValueError("Pas de variable sortante possible (ratios non définis).")
    
    min_ratio, index2 = min(Ration)  #
    return index2

def effectuer_pivot(Mat, pivot_row_index, pivot_col_index):
    pivot = Mat[pivot_row_index][pivot_col_index]
    
    for j in range(len(Mat[0])):
        Mat[pivot_row_index][j] /= pivot

    for i in range(len(Mat)):
        if i != pivot_row_index:
            multiplier = Mat[i][pivot_col_index]
            for j in range(len(Mat[0])):
                Mat[i][j] -= multiplier * Mat[pivot_row_index][j]

def verifier_solution_optimale(Mat):
    return all(x <= 0 for x in Mat[0][2:])

def simplexe(N, M):
    """Fonction principale pour exécuter l'algorithme du Simplex."""
    Mat = saisir_matrice(N, M)
    
    while not verifier_solution_optimale(Mat):
        print("Matrice actuelle:")
        for row in Mat:
            print(row)

        # Chercher la variable entrante
        Pline = chercher_variable_entrante(Mat)
        print(f"Variable entrante: {Pline}")

        # Chercher la variable sortante
        Pcol = chercher_variable_sortante(Mat, Pline)
        print(f"Variable sortante: {Pcol}")

        # Effectuer le pivot
        effectuer_pivot(Mat, Pcol, Pline)

    print("Solution optimale trouvée:")
    for row in Mat:
        print(row)

# Saisir les dimensions de la matrice
N = int(input('Nombre de lignes: '))
M = int(input('Nombre de colonnes: '))

# Exécuter l'algorithme du Simplex
simplexe(N, M)
