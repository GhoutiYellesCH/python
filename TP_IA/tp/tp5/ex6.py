from ortools.sat.python import cp_model


def solve_task_assignment():

    durations = [
        [9, 2, 7, 8],
        [5, 10, 3, 6],
        [4, 7, 8, 5],
        [3, 6, 4, 9]
    ]


    num_workers = len(durations)
    num_tasks = len(durations[0])


    model = cp_model.CpModel()


    x = {}
    for i in range(num_workers):
        for j in range(num_tasks):
            x[i, j] = model.NewIntVar(0, 1, f'worker_{i}_task_{j}')


    for j in range(num_tasks):
        model.Add(sum(x[i, j] for i in range(num_workers)) == 1)


    for i in range(num_workers):
        model.Add(sum(x[i, j] for j in range(num_tasks)) == 1)

    worker_times = [model.NewIntVar(0, 100, f'worker_{i}_time') for i in range(num_workers)]

    for i in range(num_workers):
        model.Add(worker_times[i] ==
                  sum(x[i, j] * durations[i][j] for j in range(num_tasks)))

    makespan = model.NewIntVar(0, 100, 'makespan')
    for i in range(num_workers):
        model.Add(worker_times[i] <= makespan)

    model.Minimize(makespan)

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print("Affectation optimale des tâches :")
        for i in range(num_workers):
            for j in range(num_tasks):
                if solver.Value(x[i, j]) == 1:
                    print(f"Ouvrier {chr(65 + i)} réalise la tâche J{j + 1} en {durations[i][j]} heures")

        print(f"\nDurée totale de réalisation : {solver.Value(makespan)} heures")
    else:
        print('Aucune solution trouvée')


solve_task_assignment()