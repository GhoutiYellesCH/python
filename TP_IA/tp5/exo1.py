from ortools.sat.python import cp_model

model = cp_model.CpModel()

# Create variables
x = model.NewIntVar(0, 10, "x")
y = model.NewIntVar(0, 10, "y")
z = model.NewIntVar(0, 10, "z")

# Add constraints
model.Add(x + y == z)
model.Add(x * y == z)

# Solve the model
solver = cp_model.CpSolver()
status = solver.Solve(model)

# Display results
if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print(f"x = {solver.Value(x)}, y = {solver.Value(y)}, z = {solver.Value(z)}")
else:
    print("No solution found.")
