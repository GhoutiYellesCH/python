from ortools.sat.python import cp_model

model = cp_model.CpModel()

H = model.NewIntVar(11, 24, 'H')
K = model.NewIntVar(11, 24, 'K')
L = model.NewIntVar(11, 24, 'K')
O = model.NewIntVar(11, 24, 'O')
Y = model.NewIntVar(11, 24, 'Y')

model.AddAllDifferent(H,K,O,Y)
model.Add(K==H-8)
model.Add(H!=Y)
model.Add(Y<L)
model.Add(L==H)
model.Add(H>O+10)
model.AddModuloEquality(1,(H-0),3)

solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
 print('H = %i' % solver.Value(H))
 print('K = %i' % solver.Value(K))
 print('L = %i' % solver.Value(L))
 print('O = %i' % solver.Value(O))
 print('Y = %i' % solver.Value(Y))
else:
 print('No solution found.')