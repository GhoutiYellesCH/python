from ortools.sat.python import cp_model


def solve_csp():

    model = cp_model.CpModel()


    x = model.NewIntVar(0, 5, 'x')
    y = model.NewIntVarFromDomain(cp_model.Domain.FromValues([2, 3, 8]), 'y')
    z = model.NewIntVar(0, 10, 'z')


    model.Add(x + y + z >= 20)


    xy = model.NewIntVar(0, 5 * 8, 'xy')
    x_squared = model.NewIntVar(0, 25, 'x_squared')
    xyz = model.NewIntVar(0, 5 * 8 * 10, 'xyz')

    model.AddMultiplicationEquality(xy, [x, y])
    model.AddMultiplicationEquality(x_squared, [x, x])
    model.AddMultiplicationEquality(xyz, [x, y, z])

    model.Add(xy + x_squared + xyz == 425)


    solver = cp_model.CpSolver()
    status = solver.Solve(model)


    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f'x = {solver.Value(x)}')
        print(f'y = {solver.Value(y)}')
        print(f'z = {solver.Value(z)}')
    else:
        print('No solution found')


solve_csp()