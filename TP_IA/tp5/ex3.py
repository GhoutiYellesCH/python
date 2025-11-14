from ortools.sat.python import cp_model


def solve_safe_combination():
    model = cp_model.CpModel()

    digits = [model.NewIntVar(1, 9, f"digit_{i+1}") for i in range(9)]
    # Tous les chiffres sont dans la plage 1..9

    model.AddAllDifferent(digits)
    # Tous les chiffres sont différents

    for i in range(9):
        model.Add(digits[i] != i + 1)
    # Tous les chiffres sont dans la plage 1..9

    model.Add(digits[3] - digits[5] == digits[6])
    # La différence entre le 4e et le 6e chiffre est égale au 7e chiffre

    product_first_three = model.NewIntVar(1, 9 * 9 * 9, "product_first_three")
    model.AddMultiplicationEquality(
        product_first_three, [digits[0], digits[1], digits[2]]
    )
    sum_last_two = model.NewIntVar(2, 18, "sum_last_two")
    model.Add(sum_last_two == digits[7] + digits[8])
    model.Add(product_first_three == sum_last_two)
    # La différence entre le 4e et le 6e chiffre est égale au 7e chiffre

    sum_mid_digits = model.NewIntVar(3, 27, "sum_mid_digits")
    model.Add(sum_mid_digits == digits[1] + digits[2] + digits[5])
    model.Add(sum_mid_digits < digits[7])
    # La somme des 2ème, 3ème et 6ème chiffres est inférieure au 8ème chiffre

    model.Add(digits[8] < digits[7])
    # Le dernier chiffre est également inférieur au 8ème chiffre

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        combination = [solver.Value(digit) for digit in digits]
        print("Safe Combination:", "".join(map(str, combination)))
    else:
        print("No solution found")


solve_safe_combination()

