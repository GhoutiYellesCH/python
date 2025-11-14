import math

def rec_dichotomie(f, a, b, tol, iterations=None, iteration_number=0):
    if iterations is None:
        iterations = []
    if f(a) * f(b) >= 0:
        raise ValueError("La fonction doit avoir des signes opposés aux bornes a et b.")

    c = (a + b) / 2.0
    iterations.append((iteration_number, c))
    iteration_number += 1
    
    if abs(b - a) <= tol:
        return c, iterations
    elif f(a) * f(c) < 0:
        return rec_dichotomie(f, a, c, tol, iterations, iteration_number)
    else:
        return rec_dichotomie(f, c, b, tol, iterations, iteration_number)

def rec_point_fixe(choice, x0, tol, iterations=None, iteration_number=0):
    if iterations is None:
        iterations = []

    if choice == 1:
        x1 = g1(x0)
    elif choice == 2:
        x1 = g2(x0)
    elif choice == 3:
        x1 = g3(x0)

    iterations.append((iteration_number, x1))
    iteration_number += 1
    
    if abs(x1 - x0) < tol:
        return x1, iterations
    return rec_point_fixe(choice, x1, tol, iterations, iteration_number)

def rec_newton(f, df, x0, tol, iterations=None, iteration_number=0):
    if iterations is None:
        iterations = []

    x1 = x0 - f(x0) / df(x0)
    iterations.append((iteration_number, x1))
    iteration_number += 1
    
    if abs(x1 - x0) < tol:
        return x1, iterations
    return rec_newton(f, df, x1, tol, iterations, iteration_number)

def dichotomie(f, a, b, tol):
    if f(a) * f(b) >= 0:
        raise ValueError("La fonction doit avoir des signes opposés aux bornes a et b.")

    iterations = []
    iteration_number = 0
    while (b - a) > tol:
        c = (a + b) / 2.0
        iterations.append((iteration_number, c))
        iteration_number += 1
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c, iterations

def point_fixe(choice, x0, tol):
    iterations = []
    choice = int(choice)
    iteration_number = 0
    while True:
        if choice == 1:
            x1 = g1(x0)
        elif choice == 2:
            x1 = g2(x0)
        elif choice == 3:
            x1 = g3(x0)

        iterations.append((iteration_number, x1))
        iteration_number += 1
        
        if abs(x1 - x0) < tol:
            return x1, iterations
        x0 = x1

def newton(f, df, x0, tol):
    iterations = []
    iteration_number = 0
    while True:
        x1 = x0 - f(x0) / df(x0)
        iterations.append((iteration_number, x1))
        iteration_number += 1
        
        if abs(x1 - x0) < tol:
            return x1, iterations
        x0 = x1

def f1(x):
    return x**3 + 4 * x - 2

def df1(x):
    return 3 * x**2 + 4

def f2(x):
    return math.exp(x) - 2 * x - 1

def df2(x):
    return math.exp(x) - 2

def f3(x):
    return x - math.cos(x)

def df3(x):
    return 1 + math.sin(x)

def g1(x):
    return (-(x**3) + 2) / 4

def g2(x):
    return math.log(2 * x + 1)

def g3(x):
    return math.cos(x)

def menu_fonction():
    print("\nChoisissez une fonction:")
    print("1. f1(x) = x^3 + 4x - 2")
    print("2. f2(x) = e^x - 2x - 1")
    print("3. f3(x) = x - cos(x)")
    print("0. Quitter")
    return int(input("Entrez le numéro de la fonction choisie: "))

def menu_methode():
    print("\nChoisissez une méthode:")
    print("1. Méthode de la dichotomie")
    print("2. Méthode du point fixe")
    print("3. Méthode de Newton")
    print("0. Retour au menu des fonctions")
    return int(input("Entrez le numéro de la méthode choisie: "))

def menu_meth():
    print("\nChoisissez une méthode :")
    print("1. version récursive")
    print("2. version itérative")
    print("3. Quitter")
    return int(input("Votre choix :"))

def display_iterations(iterations):
    print("\nItérations:")
    print(f"{'Numéro':<10} {'Valeur':<10}")
    for iteration, value in iterations:
        print(f"{iteration:<10} {value:<10}")

def display_function_info(f, interval, tol, x0):
    print(f"\nFonction choisie: {f.__name__} sur l'intervalle {interval} avec tolérance {tol}")
    print(f"Valeur initiale (x0): {x0}")
    print(f"Définition de la fonction: {f.__code__.co_name} = {f.__code__.co_varnames}")

def main():
    while True:
        fonction_choisie = menu_fonction()

        if fonction_choisie == 0:
            break

        if fonction_choisie == 1:
            f = f1
            df = df1
            intervalle = (0, 1)
            tol = 1e-8
            x0 = 1
        elif fonction_choisie == 2:
            f = f2
            df = df2
            intervalle = (1, 2)
            tol = 1e-4
            x0 = 2
        elif fonction_choisie == 3:
            f = f3
            df = df3
            intervalle = (0, 1)
            tol = 1e-5
            x0 = 1
        else:
            print("Choix invalide.")
            continue

        while True:
            methode_choisie = menu_methode()

            if methode_choisie == 0:
                break

            if methode_choisie == 1:
                print(f"Résolution de la fonction choisie avec la méthode de la dichotomie sur l'intervalle {intervalle}")
                while True:
                    meth = menu_meth()
                    if meth == 2:
                        racine, iterations = dichotomie(f, intervalle[0], intervalle[1], tol)
                        display_function_info(f, intervalle, tol, x0)
                        print("Racine:", racine)
                        display_iterations(iterations)
                    elif meth == 1:
                        racine, iterations = rec_dichotomie(f, intervalle[0], intervalle[1], tol)
                        display_function_info(f, intervalle, tol, x0)
                        print("Racine:", racine)
                        display_iterations(iterations)
                    elif meth == 3:
                        break

            elif methode_choisie == 2:
                print(f"Résolution de la fonction choisie avec la méthode du point fixe.")
                while True:
                    meth = menu_meth()
                    if meth == 2:
                        racine, iterations = point_fixe(fonction_choisie, x0, tol)
                        display_function_info(f, intervalle, tol, x0)
                        print("Racine:", racine)
                        display_iterations(iterations)
                    elif meth == 1:
                        racine, iterations = rec_point_fixe(fonction_choisie, x0, tol)
                        display_function_info(f, intervalle, tol, x0)
                        print("Racine:", racine)
                        display_iterations(iterations)
                    elif meth == 3:
                        break

            elif methode_choisie == 3:
                print(f"Résolution de la fonction choisie avec la méthode de Newton.")
                while True:
                    meth = menu_meth()
                    if meth == 2:
                        racine, iterations = newton(f, df, x0, tol)
                        display_function_info(f, intervalle, tol, x0)
                        print("Racine:", racine)
                        display_iterations(iterations)
                    elif meth == 1:
                        racine, iterations = rec_newton(f, df, x0, tol)
                        display_function_info(f, intervalle, tol, x0)
                        print("Racine:", racine)
                        display_iterations(iterations)
                    elif meth == 3:
                        break
            else:
                print("Choix invalide.")

if __name__ == "__main__":
    main()

