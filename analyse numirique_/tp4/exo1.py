import numpy as np

# A = [[10, 5, 5, 0], [2, 5, 7, 4], [4, 4, 1, 4], [-2, -2, 1, -3]]
# B = [25, 1, 12, 10]
A = [[1, 6, 9], [2, 1, 2], [3, 6, 9]]
B = [1, 2, 3]
X = []


def read_linear_system():
    n = int(input("Entrez le nombre d'équations: "))
    A = []
    B = []
    for i in range(n):
        print(f"Entrez les coefficients de l'équation {i + 1}:")
        A.append([float(x) for x in input().split()])
        B.append(float(input(f"Entrez le résultat de l'équation {i + 1}: ")))
    return A, B


def display_linear_system(A, B):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(f"{A[i][j]:.2f}", end=" ")
        print("|", B[i])


def algo_of_desec(A, B):
    X = [0] * len(A)
    X[0] = B[0] / A[0][0]
    for i in range(1, len(A)):
        s = 0
        for j in range(i):
            s += A[i][j] * X[j]
        X[i] = (B[i] - s) / A[i][i]
    return X


def algo_of_recur(A, B):
    X = [0] * len(A)
    X[len(A) - 1] = B[len(A) - 1] / A[len(A) - 1][len(A) - 1]
    for j in range(len(A) - 2, -1, -1):
        s = 0
        for k in range(j + 1, len(A)):
            s += A[j][k] * X[k]
        X[j] = (B[j] - s) / A[j][j]
    return X


def gauss_elimination_pivot(A, B):
    n = len(A)
    for i in range(0, n):
        m = A[i][i]
        if m != 0:
            for j in range(i + 1, n):
                q = A[j][i]
                A[j][i] = 0
                B[j] = B[j] - (q / m) * B[i]
            for l in range(i + 1, n):
                A[j][l] = A[j][l] - (q / m) * A[j][l]
        else:
            print("division par zero")
        print("itiration")
        display_linear_system(A, B)
    return algo_of_recur(A, B)


def gaussian_elimination_partial_pivot(A, b):
    n = len(A)
    m = len(A[0])
    A = A.copy().astype(float)
    b = b.copy().astype(float)

    print("* Le systeme est :")
    display_linear_system(A, b)

    for k in range(1, n + 1):
        p = abs(A[k - 1, k - 1])
        l = k - 1

        for i in range(k - 1, n):
            if abs(A[i, k - 1]) > p:
                p = abs(A[i, k - 1])
                l = i

        if l != k - 1:
            for j in range(k - 1, m):
                temp = A[k - 1, j]
                A[k - 1, j] = A[l, j]
                A[l, j] = temp
            temp = b[k - 1]
            b[k - 1] = b[l]
            b[l] = temp

        print(f"\n* Iteration K= {k} :")

        for i in range(k, n):
            q = A[i, k - 1] / A[k - 1, k - 1]
            A[i, k - 1] = 0
            for j in range(k, m):
                A[i, j] = A[i, j] - A[k - 1, j] * q
            b[i] = b[i] - b[k - 1] * q

        display_linear_system(A, b)

    return A, b


def gaussian_elimination_partial_pivot_recursive(A, b, k=0):
    n = len(A)

    if k == 0:
        A = A.copy().astype(float)
        b = b.copy().astype(float)
        print("* Le systeme est :")
        display_linear_system(A, b)

    if k == n - 1:
        return A, b

    pivot_row = k + np.argmax(np.abs(A[k:, k]))
    pivot_value = A[pivot_row, k]

    if pivot_row != k:
        A[[k, pivot_row]] = A[[pivot_row, k]]
        b[k], b[pivot_row] = b[pivot_row], b[k]

    print(f"\n* Iteration K= {k+1} :")

    factors = A[k + 1 :, k] / pivot_value
    A[k + 1 :, k] = 0
    A[k + 1 :, k + 1 :] -= np.outer(factors, A[k, k + 1 :])
    b[k + 1 :] -= factors * b[k]

    display_linear_system(A, b)

    return gaussian_elimination_partial_pivot_recursive(A, b, k + 1)


def gauss_jordan_elimination_total_pivot(A, b):
    n = len(A)
    A = A.copy().astype(float)
    b = b.copy().astype(float)

    print("* Le systeme initial est :")
    display_linear_system(A, b)

    for k in range(n):
        max_element = 0
        max_row = k
        max_col = k
        for i in range(k, n):
            for j in range(k, n):
                if abs(A[i, j]) > max_element:
                    max_element = abs(A[i, j])
                    max_row = i
                    max_col = j

        if max_row != k:
            A[[k, max_row]] = A[[max_row, k]]
            b[k], b[max_row] = b[max_row], b[k]
        if max_col != k:
            A[:, [k, max_col]] = A[:, [max_col, k]]

        print(f"\n* Iteration K= {k+1} :")

        if abs(A[k, k]) < 1e-10:
            raise ValueError("Matrix is singular or nearly singular")

        # Make the pivot element 1
        pivot = A[k, k]
        A[k] = A[k] / pivot
        b[k] = b[k] / pivot

        # Eliminate the variable from all other equations
        for i in range(n):
            if i != k:
                factor = A[i, k]
                A[i] = A[i] - factor * A[k]
                b[i] = b[i] - factor * b[k]

        display_linear_system(A, b)

    return A, b


def lu_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        L[i][i] = 1

        for j in range(i, n):
            U[i][j] = A[i][j]
            for k in range(i):
                U[i][j] -= L[i][k] * U[k][j]

        for j in range(i + 1, n):
            L[j][i] = A[j][i]
            for k in range(i):
                L[j][i] -= L[j][k] * U[k][i]
            L[j][i] /= U[i][i]

    return L, U


def forward_substitution(L, b):
    n = len(b)
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i][j] * y[j]
    return y


def backward_substitution(U, y):
    n = len(y)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = y[i]
        for j in range(i + 1, n):
            x[i] -= U[i][j] * x[j]
        x[i] /= U[i][i]
    return x


def print_system(A, b):
    n = len(A)
    for i in range(n):
        row = [f"{A[i,j]:6.4f}" for j in range(n)]
        print(f"[ {' '.join(row)} : {b[i]:6.4f} ]")


def solve_linear_system_lu(A, b):
    print("* Le systeme initial est :")
    print_system(A, b)

    try:
        L, U = lu_decomposition(A)

        print("\n-------- Décomposition LU --------")
        print("\n* Matrice L :")
        print_system(L, np.zeros(len(b)))
        print("\n* Matrice U :")
        print_system(U, np.zeros(len(b)))

        y = forward_substitution(L, b)
        print("\n* Résolution de Ly = b (descente) :")
        for i, val in enumerate(y):
            print(f"y_{i+1} = {val:.6f}")

        x = backward_substitution(U, y)
        print("\n* Résolution de Ux = y (remontée) :")
        for i, val in enumerate(x):
            print(f"x_{i+1} = {val:.6f}")

        return x

    except ValueError as e:
        print(f"Error solving system: {e}")
        return None


def jacobi(A, b, x0=None, tol=1e-10, max_iterations=100):
    n = len(b)
    x = [0.0] * n if x0 is None else x0.copy()

    for it_count in range(max_iterations):
        x_new = [0.0] * n
        for i in range(n):
            sum_ax = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_ax) / A[i][i]
        print(f"iteration {it_count + 1}:{x_new}")

        # Check for convergence
        if max(abs(x_new[i] - x[i]) for i in range(n)) < tol:
            print(f"Jacobi method converged in {it_count + 1} iterations.")
            return x_new
        x = x_new

    print("Jacobi method did not converge.")
    return x


def gauss_seidel(A, b, x0=None, tol=1e-10, max_iterations=100):
    n = len(b)
    x = [0.0] * n if x0 is None else x0.copy()

    for it_count in range(max_iterations):
        x_old = x.copy()
        for i in range(n):
            sum_ax = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - sum_ax) / A[i][i]
        print(f"iteration {it_count + 1}:{x_old}")

        # Check for convergence
        if max(abs(x[i] - x_old[i]) for i in range(n)) < tol:
            print(f"Gauss-Seidel method converged in {it_count + 1} iterations.")
            return x

    print("Gauss-Seidel method did not converge.")
    return x


def menu_int():
    print("\nChoisissez une fonction:")
    print("1. Lire un système linéaire")
    print("2. Afficher le système linéaire")
    print("3. Méthode directe")
    print("4. Méthode itérative")
    print("5. Quitter")
    return int(input("Entrez le numéro de la fonction choisie: "))


def menu_methode2():
    print("\nChoisissez une méthode:")
    print("1. Jacobi")
    print("2. Gauss-Seidel")
    print("0. Retour au menu principal")
    return int(input("Entrez le numéro de la méthode choisie: "))


def menu_methode():
    print("\nChoisissez une méthode:")
    print("1. Élimination de Gauss avec pivot")
    print("2. Élimination de Gauss avec pivot partielle")
    print("3. Élimination de Gauss ave  pivot totale")
    print("4. Factorisation")
    print("0. Retour au menu principal")
    return int(input("Entrez le numéro de la méthode choisie: "))


def menu_meth():
    print("\nChoisissez une méthode:")
    print("1. Version itérative")
    print("2. Version récursive")
    print("3. Quitter")
    return int(input("Votre choix: "))


def main():
    A_local, B_local = A, B

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
