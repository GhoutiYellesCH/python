from ortools.sat.python import cp_model


def solve_csp():

    model = cp_model.CpModel()


    x = model.NewIntVar(0, 10, 'x')
    y = model.NewIntVar(0, 10, 'y')
    z = model.NewIntVar(0, 10, 'z')


    model.Add(x + y == z)


    xy = model.NewIntVar(0, 100, 'xy')
    model.AddMultiplicationEquality(xy, [x, y])
    model.Add(xy == z)


    solver = cp_model.CpSolver()
    status = solver.Solve(model)


    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f'x = {solver.Value(x)}')
        print(f'y = {solver.Value(y)}')
        print(f'z = {solver.Value(z)}')
    else:
        print('No solution found')


solve_csp()