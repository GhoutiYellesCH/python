from ortools.sat.python import cp_model

def solve_safe_combination():
    model = cp_model.CpModel()


    digits = [model.NewIntVar(1, 9, f'digit_{i+1}') for i in range(9)]


    model.AddAllDifferent(digits)


    for i in range(9):
        model.Add(digits[i] != i+1)


    model.Add(digits[3] - digits[5] == digits[6])


    product_first_three = model.NewIntVar(1, 9*9*9, 'product_first_three')
    model.AddMultiplicationEquality(
        product_first_three,
        [digits[0], digits[1], digits[2]]
    )
    sum_last_two = model.NewIntVar(2, 18, 'sum_last_two')
    model.Add(sum_last_two == digits[7] + digits[8])
    model.Add(product_first_three == sum_last_two)


    sum_mid_digits = model.NewIntVar(3, 27, 'sum_mid_digits')
    model.Add(sum_mid_digits == digits[1] + digits[2] + digits[5])
    model.Add(sum_mid_digits < digits[7])


    model.Add(digits[8] < digits[7])


    solver = cp_model.CpSolver()
    status = solver.Solve(model)


    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        combination = [solver.Value(digit) for digit in digits]
        print("Safe Combination:", ''.join(map(str, combination)))
    else:
        print('No solution found')

solve_safe_combination()