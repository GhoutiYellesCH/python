from ortools.sat.python import cp_model
import numpy as np
import matplotlib.pyplot as plt

model = cp_model.CpModel()

matrix = np.array([[model.NewIntVarFromDomain(cp_model.Domain.FromValues([0,1]), f'cell[{i}][{j}]')
                    for j in range(8)] for i in range(8)])

for row in range(8):
    model.Add(sum(matrix[i][row] for i in range(8)) == 1)

for col in range(8):
    model.Add(sum(matrix[col][i] for i in range(8)) == 1)

model.Add(sum(matrix[i][i] for i in range(8)) == 1)
model.Add(sum(matrix[i][8-1-i] for i in range(8)) == 1)

for k in range(-7, 8):
    model.Add(sum(np.diag(matrix, k)) <= 1)

for k in range(-7, 8):
    model.Add(sum(np.diag(np.fliplr(matrix), k)) <= 1)

solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print("Solution found:")
    solution = np.zeros((8, 8), dtype=int)
    for i in range(8):
        for j in range(8):
            value = solver.Value(matrix[i][j])
            solution[i][j] = value
            print(value, end="\t")
        print("\n")


    fig, ax = plt.subplots(figsize=(8, 8))


    ax.set_xlim(0, 8)
    ax.set_ylim(0, 8)

    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                ax.add_patch(plt.Rectangle((j, i), 1, 1, facecolor='#769656'))
            else:
                ax.add_patch(plt.Rectangle((j, i), 1, 1, facecolor='#eeeed2'))

    for i in range(8):
        for j in range(8):
            if solution[i][j] == 1:
                ax.add_patch(plt.Circle((j+0.5, 7-i+0.5), 0.3, facecolor='red', edgecolor='black'))

    ax.set_title('8-Queens Problem Solution')
    plt.show()
else:
    print("No solution found.")
