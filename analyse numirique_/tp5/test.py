import math


def lagrange_basis(j, x, points):
    numerator = 1.0
    denominator = 1.0
    xj, yj = points[j]

    for i in range(len(points)):
        xi, yi = points[i]
        if i != j:
            numerator *= x - xi
            denominator *= xj - xi

    return numerator / denominator


def lagrange_interpolation(points, x):

    result = 0.0
    for j in range(len(points)):
        xj, yj = points[j]
        result += yj * lagrange_basis(j, x, points)

    return result


def newton_interpolation(points, x):

    n = len(points)

    diff_divided = points[:]
    for i in range(1, n):
        for j in range(n - i):
            diff_divided[j] = (diff_divided[j + 1] - diff_divided[j]) / (
                points[i + j][0] - points[j][0]
            )

    # Calculer la valeur de la fonction interpolée
    result = diff_divided[0]
    h = x - points[0][0]
    for i in range(1, n):
        result += (h * diff_divided[i]) / math.factorial(i)

    return result


def newton_divided_difference(points):
    """
    points : liste de tuples (x_i, y_i), où chaque tuple représente un point (x_i, f(x_i))
    Renvoie la table des différences divisées
    """
    n = len(points)

    if n == 1:
        return points[0][1]

    diff_divided = []
    for i in range(1, n):
        diff_divided.append(
            (points[i][1] - points[i - 1][1]) / (points[i][0] - points[i - 1][0])
        )

    return [points[0][1]] + newton_divided_difference(diff_divided)


def newton_interpolation_recursive(points, x):
    """
    points : liste de tuples (x_i, y_i), où chaque tuple représente un point (x_i, f(x_i))
    x : le point où nous voulons estimer la valeur de la fonction
    """

    n = len(points)
    diff_divided = newton_divided_difference(points)

    def helper(i, j):
        if i == 1:
            return diff_divided[j - 1]

        return (helper(1, j + 1) - helper(1, j)) / (
            points[i + j - 2][0] - points[i - 1][0]
        )

    result = diff_divided[0]
    h = x - points[0][0]
    for i in range(1, n):
        result += (h * helper(i, 1)) / math.factorial(i)

    return result


def add_point(points, new_point):

    points.append(new_point)
    points.sort(key=lambda p: p[0])
    return points


def main_menu():
    while True:
        print("\nMenu Principal")
        print("1. Interpolation Lagrange")
        print("2. Interpolation Newton (Non-récursif)")
        print("3. Interpolation Newton (Récursif)")
        print("4. Ajouter un point d'appui")
        print("0. Quitter")

        choice = input("Choisissez une option : ")

        if choice == "1":
            points = [(1, 2), (4, 3), (6, 5)]
            x_to_interpolate = float(
                input(
                    "Entrez le point x où vous voulez estimer la valeur de la fonction : "
                )
            )
            result = lagrange_interpolation(points, x_to_interpolate)
            print(
                f"La valeur estimée de la fonction en {x_to_interpolate} est : {result}"
            )

        elif choice == "2":
            points = [(1, 2), (4, 3), (6, 5)]
            x_to_interpolate = float(
                input(
                    "Entrez le point x où vous voulez estimer la valeur de la fonction : "
                )
            )
            result = newton_interpolation(points, x_to_interpolate)
            print(
                f"La valeur estimée de la fonction en {x_to_interpolate} est : {result}"
            )

        elif choice == "3":
            points = [(1, 2), (4, 3), (6, 5)]
            x_to_interpolate = float(
                input(
                    "Entrez le point x où vous voulez estimer la valeur de la fonction : "
                )
            )
            result = newton_interpolation_recursive(points, x_to_interpolate)
            print(
                f"La valeur estimée de la fonction en {x_to_interpolate} est : {result}"
            )

        elif choice == "4":
            points = [(1, 2), (4, 3), (6, 5)]
            new_point = tuple(
                map(float, input("Entrez le nouveau point (x y) : ").split())
            )
            points = add_point(points, new_point)
            print(f"Le point {new_point} a été ajouté à la liste.")

        elif choice == "0":
            break

        else:
            print("Option invalide. Veuillez choisir une option valide.")


if __name__ == "__main__":
    main_menu()
