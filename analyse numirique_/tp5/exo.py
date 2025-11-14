
def read_point():

def lagrange_basis(j, x, points):
    numerator = 1.0
    denominator = 1.0
    xj, yj = points[j]

    for i in range(len(points)):
        xi, yi = points[i]
        if i != j:
            numerator *= (x - xi)
            denominator *= (xj - xi)

    return numerator / denominator


def lagrange_interpolation(points, x):

    result = 0.0
    for j in range(len(points)):
        xj, yj = points[j]
        result += yj * lagrange_basis(j, x, points)

    return result

# Exemple d'utilisation
points = [(1, 2), (4, 3), (6, 5)]
x_to_interpolate = 3
result = lagrange_interpolation(points, x_to_interpolate)
print(f"La valeur estimée de la fonction en {x_to_interpolate} est : {result}")
def menu_int():
    print(" \n menu ")
    print("1. lire les point d'appui")
    print("2. Afficher les point d'appui ")
    print("3. Interpretation LAGRONGE ")
    print("4. Interpretation NEWTON")
    print("5. Quitter")
    return int(input("Entrez le numéro de la fonction choisie: "))

def main():

    while True:
        choice = menu_int()
        if choice == 1:
            A_local, B_local = read_linear_system()
        elif choice == 2:
            display_linear_system(A_local, B_local)
        elif choice == 3:
            while True:
                methode_choisie = menu_methode()
                if methode_choisie == 0:
                    break
                elif methode_choisie == 1:
                    print("Méthode de Gauss avec pivot")
                    while True:
                        meth = menu_meth()
                        if meth == 1:
                            result = gauss_elimination_pivot(A_local, B_local)
                            print(f"\nSolution itérative: {result}")
                        elif meth == 2:
                            print("Méthode récursive non implémentée")
                        elif meth == 3:
                            break
                        else:
                            print("Choix invalide.")
                elif methode_choisie == 2:
                    print("Méthode d'élimination partielle")
                    while True:
                        meth = menu_meth()
                        if meth == 1:
                            result = gaussian_elimination_partial_pivot(
                                A_local, B_local
                            )
                            print(f"\nSolution itérative: {result}")
                        elif meth == 2:
                            result = gaussian_elimination_partial_pivot_recursive(
                                A_local, B_local
                            )
                        elif meth == 3:
                            break
                        else:
                            print("Choix invalide.")
                elif methode_choisie == 3:
                    print("Méthode d'élimination totale")
                    while True:
                        meth = menu_meth()
                        if meth == 1:
                            result = gauss_jordan_elimination_total_pivot(
                                A_local, B_local
                            )
                            print(f"\nSolution itérative: {result}")
                        elif meth == 2:
                            print("Méthode récursive non implémentée")
                        elif meth == 3:
                            break

                elif methode_choisie == 4:
                    print("Méthode de factorisation")
                    while True:
                        meth = menu_meth()
                        if meth == 1:
                            result = solve_linear_system_lu(A_local, B_local)
                            print(f"\nSolution itérative: {result}")
                        elif meth == 2:
                            print("Méthode récursive non implémentée")
                        elif meth == 3:
                            break

                else:
                    print("Choix invalide.")
        elif choice == 4:
            while True:
                methode_choisie = menu_methode2()
                if methode_choisie == 0:
                    break
                elif methode_choisie == 1:
                    print("Méthode de Jacobi")
                    result = jacobi(A_local, B_local)
                    print(f"\nSolution itérative: {result}")
                elif methode_choisie == 2:
                    print("Méthode de Gauss-Seidel")
                    result = gauss_seidel(A_local, B_local)
                    print(f"\nSolution itérative: {result}")
                else:
                    print("Choix invalide")
        elif choice == 5:
            print("Au revoir!")
            break
        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()
