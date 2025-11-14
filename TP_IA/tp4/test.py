# import cp_model library
from ortools.sat.python import cp_model

# création d'un modèle.
model = cp_model.CpModel()
# Déclaration de la variable x, elle prend des valeurs entre 0 et 5
x = model.NewIntVar(0, 5, "x")
# Déclaration de la variable y, elle prend les valeurs 2,3 ou 8
y = model.NewIntVarFromDomain(cp_model.Domain.FromValues([2, 3, 8]), "y")
# déclaration des contraintes:
model.Add(x + y < 5)
model.Add(x != y)
# déclaration du solveur et recherche des solutions
solver = cp_model.CpSolver()
status = solver.Solve(model)
# affichage d'une solution si elle existe.
if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print("x = %i" % solver.Value(x))
    print("y = %i" % solver.Value(y))
else:
    print("No solution found.")
