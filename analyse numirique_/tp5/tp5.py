def lagrange_interpolation(x_values, y_values, x):
    n = len(x_values)
    result = 0.0
    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if j != i:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term
    return result


def divided_difference(x_values, y_values):
    n = len(y_values)
    coef = [0] * n
    for i in range(n):
        coef[i] = y_values[i]

    for j in range(1, n):
        for i in range(n - j):
            coef[i] = (coef[i + 1] - coef[i]) / (x_values[i + j] - x_values[i])

    return coef


def newton_interpolation(x_values, y_values, x):
    coef = divided_difference(x_values, y_values)
    n = len(coef)
    result = coef[0]
    for i in range(1, n):
        term = coef[i]
        for j in range(i):
            term *= x - x_values[j]
        result += term
    return result


def add_point(x_values, y_values):
    x = float(input("Enter the x value of the new point: "))
    y = float(input("Enter the y value of the new point: "))
    x_values.append(x)
    y_values.append(y)
    print(f"Point ({x}, {y}) added.")


def display_points(x_values, y_values):
    print("Current points:")
    for x, y in zip(x_values, y_values):
        print(f"({x}, {y})")


def main():
    x_values = []
    y_values = []

    while True:
        print("\nMenu:")
        print("1. Add a point")
        print("2. Display points")
        print("3. Lagrange Interpolation")
        print("4. Newton Interpolation")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_point(x_values, y_values)
        elif choice == "2":
            display_points(x_values, y_values)
        elif choice == "3":
            if len(x_values) == 0:
                print("No points available for interpolation.")
                continue
            x = float(input("Enter the value of x for Lagrange interpolation: "))
            result = lagrange_interpolation(x_values, y_values, x)
            print(f"Lagrange Interpolation result at x={x}: {result}")
        elif choice == "4":
            if len(x_values) == 0:
                print("No points available for interpolation.")
                continue
            x = float(input("Enter the value of x for Newton interpolation: "))
            result = newton_interpolation(x_values, y_values, x)
            print(f"Newton Interpolation result at x={x}: {result}")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
