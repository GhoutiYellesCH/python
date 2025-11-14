from ortools.sat.python import cp_model


def solve_task_scheduling():

    # variable
    # les temps d'exution
    #
    # la cantraint de tach fin[i] = start[i] + duree[i]
    #
    # T1 -> T2
    # T3 -> T4
    # T2 -> T4
    # T4 -> T5
    #
    # makepen = max ( ends[i] )
    #
    # min(makepen)
    #

    durations = [3, 2, 3, 1, 2]

    model = cp_model.CpModel()

    num_tasks = len(durations)

    starts = [model.NewIntVar(0, 20, f"start_{i}") for i in range(num_tasks)]
    ends = [model.NewIntVar(0, 20, f"end_{i}") for i in range(num_tasks)]
    makespan = model.NewIntVar(0, 20, "makespan")

    for i in range(num_tasks):
        model.Add(ends[i] == starts[i] + durations[i])

    model.Add(starts[1] >= ends[0])
    model.Add(starts[3] >= ends[1])
    model.Add(starts[3] >= ends[2])
    model.Add(starts[4] >= ends[3])

    model.AddMaxEquality(makespan, ends)

    model.Minimize(makespan)

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print("Optimal Task Schedule:")
        for i in range(num_tasks):
            print(
                f"Task {i + 1}: Start Time = {solver.Value(starts[i])}, "
                f"End Time = {solver.Value(ends[i])}"
            )
        print(f"Total Project Duration: {solver.Value(makespan)} hours")
    else:
        print("No solution found")


solve_task_scheduling()

