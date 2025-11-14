from ortools.sat.python import cp_model


model = cp_model.CpModel()


x = model.NewIntVar(0, 10, 'x')  #
y = model.NewIntVarFromDomain(cp_model.Domain.FromValues([2, 3, 8]), 'y')
z = model.NewIntVar(1, 8, 'z')


model.Add(x + y == 8)
model.Add(x > y)
model.Add(z + y <= x)


solver = cp_model.CpSolver()
status = solver.Solve(model)


if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print("Solutions trouvées :")
    print(f"x = {solver.Value(x)}, y = {solver.Value(y)}, z = {solver.Value(z)}")

    assert solver.Value(x) + solver.Value(y) == 8, "Erreur : Contrainte x + y == 8 non respectée"
    assert solver.Value(x) > solver.Value(y), "Erreur : Contrainte x > y non respectée"
    assert solver.Value(z) + solver.Value(y) <= solver.Value(x), "Erreur : Contrainte z + y <= x non respectée"
else:
    print("Pas de solution trouvée.")
