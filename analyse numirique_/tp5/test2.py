import numpy as np


def read_point(n):
    points = []
    for i in range(n + 1):
        xi = float(input(f"Entrez x{i}: "))
        yi = float(input(f"Entrez y{i}: "))
        points.append((xi, yi))
    return points


def lagrange_interpolation(points, x):
    n = len(points) - 1
    p = 0

    for i in range(n + 1):
        li = 1
        for j in range(n + 1):
            if i != j:
                li *= (x - points[j][0]) / (points[i][0] - points[j][0])
        p += points[i][1] * li

    return p


def newton_interpolation(points, x):
    n = len(points) - 1
    di = [point[1] for point in points]

    for j in range(1, n + 1):
        for i in range(n, j - 1, -1):
            di[i] = (di[i] - di[i - 1]) / (points[i][0] - points[i - j][0])

    p = di[n]
    for k in range(1, n + 1):
        p = p * (x - points[n - k][0]) + di[n - k]

    return p


def print_newton_table(points):
    n = len(points) - 1
    table = np.zeros((n + 1, n + 1))
    for i in range(n + 1):
        table[i][0] = points[i][1]

    for j in range(1, n + 1):
        for i in range(n, j - 1, -1):
            table[i][j] = (table[i][j - 1] - table[i - 1][j - 1]) / (
                points[i][0] - points[i - j][0]
            )

    print("Table des différences divisées:")
    for row in table:
        print(row)
    print()


def main_menu():
    while True:
        print("\nMenu principal:")
        print("1. Interpolation de Lagrange")
        print("2. Interpolation de Newton")
        print("3. Ajouter un point d'appui supplémentaire")
        print("4. Quitter")

        choice = input("Choisissez une option (1-4): ")

        if choice == "1":
            n = int(input("Entrez le nombre de points (n+1): "))
            points = read_point(n)

            x = float(input("Entrez le point x à évaluer: "))
            result = lagrange_interpolation(points, x)
            print(f"Valeur de f en {x} (Lagrange): {result}")

        elif choice == "2":
            n = int(input("Entrez le nombre de points (n+1): "))
            points = read_point(n)

            print_newton_table(points)

            x = float(input("Entrez le point x à évaluer: "))
            result = newton_interpolation(points, x)
            print(f"Valeur de f en {x} (Newton): {result}")

        elif choice == "3":
            n = int(input("Entrez le nombre de points actuels (n+1): "))

            xi_new = float(input("Entrez le nouveau x: "))
            yi_new = float(input("Entrez le nouveau y: "))
            points.append((xi_new, yi_new))

            print("\nPoints mis à jour:")
            for point in points:
                print(point)

        elif choice == "4":
            print("Au revoir!")
            break

        else:
            print("Option invalide. Veuillez choisir une option valide.")


if __name__ == "__main__":
    main_menu()
