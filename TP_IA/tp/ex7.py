from ortools.sat.python import cp_model

def solve_sudoku(puzzle):
    model = cp_model.CpModel()

    cells = {}
    for i in range(9):
        for j in range(9):
            cells[(i, j)] = model.NewIntVar(1, 9, f"cell_{i}_{j}")

    for i in range(9):
        model.AddAllDifferent([cells[(i, j)] for j in range(9)])

    for j in range(9):
        model.AddAllDifferent([cells[(i, j)] for i in range(9)])

    for block_row in range(3):
        for block_col in range(3):
            block_cells = [
                cells[(block_row * 3 + di, block_col * 3 + dj)]
                for di in range(3)
                for dj in range(3)
            ]
            model.AddAllDifferent(block_cells)

    for i in range(9):
        for j in range(9):
            if puzzle[i][j] != 0:
                model.Add(cells[(i, j)] == puzzle[i][j])

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
        solution = [[solver.Value(cells[(i, j)]) for j in range(9)] for i in range(9)]
        return solution
    else:
        return None


puzzle = [
    [0, 3, 0, 4, 0, 5, 0, 7, 0],
    [6, 2, 0, 0, 8, 0, 4, 0, 0],
    [7, 0, 0, 0, 0, 1, 0, 0, 9],
    [2, 0, 6, 0, 0, 3, 8, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 0, 3],
    [0, 1, 3, 6, 0, 0, 9, 5, 0],
    [0, 0, 8, 0, 4, 7, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 6],
    [0, 0, 9, 0, 5, 0, 3, 8, 2]
]

solution = solve_sudoku(puzzle)
if solution:
    for row in solution:
        print(row)
else:
    print("No solution found.")
