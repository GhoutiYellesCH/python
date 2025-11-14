from ortools.sat.python import cp_model

model = cp_model.CpModel()

S = model.NewIntVar(1, 9, 'S')
E = model.NewIntVar(0, 9, 'E')
N = model.NewIntVar(0, 9, 'N')
D = model.NewIntVar(0, 9, 'D')
M = model.NewIntVar(1, 9, 'M')
O = model.NewIntVar(0, 9, 'O')
R = model.NewIntVar(0, 9, 'R')
Y = model.NewIntVar(0, 9, 'Y')

model.AddAllDifferent([S, E, N, D, M, O, R, Y])

send = S * 1000 + E * 100 + N * 10 + D
more = M * 1000 + O * 100 + R * 10 + E
money = M * 10000 + O * 1000 + N * 100 + E * 10 + Y

model.Add(send + more == money)

solver = cp_model.CpSolver()

def print_solution():
    send_val = solver.Value(S) * 1000 + solver.Value(E) * 100 + solver.Value(N) * 10 + solver.Value(D)
    more_val = solver.Value(M) * 1000 + solver.Value(O) * 100 + solver.Value(R) * 10 + solver.Value(E)
    money_val = solver.Value(M) * 10000 + solver.Value(O) * 1000 + solver.Value(N) * 100 + solver.Value(E) * 10 + solver.Value(Y)
    print(f"S={solver.Value(S)}, E={solver.Value(E)}, N={solver.Value(N)}, D={solver.Value(D)}")
    print(f"M={solver.Value(M)}, O={solver.Value(O)}, R={solver.Value(R)}, Y={solver.Value(Y)}")

status = solver.Solve(model)


if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print("Solution trouvée:")
    print_solution()
else:
    print("Pas de solution trouvée.")