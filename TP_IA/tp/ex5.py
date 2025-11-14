from ortools.sat.python import cp_model

n = 3
model = cp_model.CpModel()
S = (n * (n**2 + 1))

square = [[model.NewIntVar(1, n**2, f'X[{i},{j}]') for j in range(n)] for i in range(n)]
model.AddAllDifferent([square[i][j] for i in range(n) for j in range(n)])
for i in range(n):
        model.Add(sum(square[i][j] for j in range(n)) == S)
for j in range(n):
        model.Add(sum(square[i][j] for i in range(n)) == S)

model.Add(sum(square[i][i] for i in range(n)) == S)

model.Add(sum(square[i][n-i-1] for i in range(n)) == S)

solver = cp_model.CpSolver()
status = solver.Solve(model)
if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:

    print(f"\nCarré magique d'ordre {n} trouvé :")
    for i in range(n):
        print([solver.Value(square[i][j]) for j in range(n)])
    print(f"S = {S}")
else:
    print(f"Pas de solution trouvée pour un carré magique d'ordre {n}.")