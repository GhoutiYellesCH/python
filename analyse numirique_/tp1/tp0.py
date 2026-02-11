def read_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input("M[%d][%d]= " % (i, j))))
        matrix.append(row)
    return matrix


def read_square_matrix(size):
    return read_matrix(size, size)


def print_matrix(matrix):
    print()
    for row in matrix:
        print("\t".join(str(value) for value in row))
    print()


def identity_matrix(size):
    return [[1 if i == j else 0 for j in range(size)] for i in range(size)]


def add_matrices(mat_a, mat_b):
    rows = len(mat_a)
    cols = len(mat_a[0])
    return [[mat_a[i][j] + mat_b[i][j] for j in range(cols)] for i in range(rows)]


def multiply_matrices(mat_a, mat_b):
    rows_a = len(mat_a)
    cols_a = len(mat_a[0])
    rows_b = len(mat_b)
    cols_b = len(mat_b[0])
    if cols_a != rows_b:
        raise ValueError("Multiplication impossible: dimensions incompatibles.")
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += mat_a[i][k] * mat_b[k][j]
    return result


def transpose_square_matrix(matrix):
    size = len(matrix)
    return [[matrix[j][i] for j in range(size)] for i in range(size)]


def is_upper_triangular(matrix):
    size = len(matrix)
    for i in range(1, size):
        for j in range(0, i):
            if matrix[i][j] != 0:
                return False
    return True


def is_lower_triangular(matrix):
    size = len(matrix)
    for i in range(size):
        for j in range(i + 1, size):
            if matrix[i][j] != 0:
                return False
    return True


def is_diagonal(matrix):
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            if i != j and matrix[i][j] != 0:
                return False
    return True


def is_symmetric(matrix):
    size = len(matrix)
    for i in range(size):
        for j in range(i + 1, size):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


def main():
    current_matrix = None
    while True:
        print("Menu")
        print("1. Lire une matrice carree")
        print("2. Afficher la matrice courante")
        print("3. Afficher une matrice identite")
        print("4. Calculer la somme de deux matrices carrees")
        print("5. Calculer le produit de deux matrices")
        print("6. Calculer la transposee de la matrice courante")
        print("7. Tester si la matrice courante est triangulaire superieure")
        print("8. Tester si la matrice courante est triangulaire inferieure")
        print("9. Tester si la matrice courante est diagonale")
        print("10. Tester si la matrice courante est symetrique")
        print("0. Quitter")
        choice = input("Votre choix: ")

        if choice == "1":
            size = int(input("Entrez la taille N: "))
            current_matrix = read_square_matrix(size)
            print("Matrice courante:")
            print_matrix(current_matrix)
        elif choice == "2":
            if current_matrix is None:
                print("Aucune matrice courante. Utilisez l'option 1 d'abord.")
            else:
                print("Matrice courante:")
                print_matrix(current_matrix)
        elif choice == "3":
            size = int(input("Entrez l'ordre N: "))
            print("Matrice identite:")
            print_matrix(identity_matrix(size))
        elif choice == "4":
            size = int(input("Entrez la taille N des matrices carrees: "))
            print("Lecture de la premiere matrice")
            mat_a = read_square_matrix(size)
            print("Lecture de la deuxieme matrice")
            mat_b = read_square_matrix(size)
            print("Somme des matrices:")
            print_matrix(add_matrices(mat_a, mat_b))
        elif choice == "5":
            rows_a = int(input("Entrez le nombre de lignes de la premiere matrice: "))
            cols_a = int(input("Entrez le nombre de colonnes de la premiere matrice: "))
            rows_b = int(input("Entrez le nombre de lignes de la deuxieme matrice: "))
            cols_b = int(input("Entrez le nombre de colonnes de la deuxieme matrice: "))
            print("Lecture de la premiere matrice")
            mat_a = read_matrix(rows_a, cols_a)
            print("Lecture de la deuxieme matrice")
            mat_b = read_matrix(rows_b, cols_b)
            try:
                print("Produit des matrices:")
                print_matrix(multiply_matrices(mat_a, mat_b))
            except ValueError as error:
                print(error)
        elif choice == "6":
            if current_matrix is None:
                print("Aucune matrice courante. Utilisez l'option 1 d'abord.")
            else:
                print("Transposee de la matrice courante:")
                print_matrix(transpose_square_matrix(current_matrix))
        elif choice == "7":
            if current_matrix is None:
                print("Aucune matrice courante. Utilisez l'option 1 d'abord.")
            else:
                print(
                    "Triangulaire superieure:"
                    if is_upper_triangular(current_matrix)
                    else "Pas triangulaire superieure."
                )
        elif choice == "8":
            if current_matrix is None:
                print("Aucune matrice courante. Utilisez l'option 1 d'abord.")
            else:
                print(
                    "Triangulaire inferieure:"
                    if is_lower_triangular(current_matrix)
                    else "Pas triangulaire inferieure."
                )
        elif choice == "9":
            if current_matrix is None:
                print("Aucune matrice courante. Utilisez l'option 1 d'abord.")
            else:
                print("Diagonale:" if is_diagonal(current_matrix) else "Pas diagonale.")
        elif choice == "10":
            if current_matrix is None:
                print("Aucune matrice courante. Utilisez l'option 1 d'abord.")
            else:
                print(
                    "Symetrique:" if is_symmetric(current_matrix) else "Pas symetrique."
                )
        elif choice == "0":
            return
        else:
            print("Choix invalide, veuillez recommencer.")


if __name__ == "__main__":
    main()
