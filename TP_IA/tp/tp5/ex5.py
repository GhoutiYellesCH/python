from ortools.sat.python import cp_model


def solve_task_scheduling():

    durations = [3, 2, 3, 1, 2]


    precedences = [(0, 2), (0, 3), (1, 4)]

    model = cp_model.CpModel()

    num_tasks = len(durations)

    start_times = [model.NewIntVar(0, 100, f'start_time_{i}') for i in range(num_tasks)]

    end_times = [model.NewIntVar(0, 100, f'end_time_{i}') for i in range(num_tasks)]

    makespan = model.NewIntVar(0, 100, 'makespan')

    for i in range(num_tasks):

        model.Add(end_times[i] == start_times[i] + durations[i])

        model.Add(end_times[i] <= makespan)

    for (pred, succ) in precedences:
        model.Add(start_times[succ] >= end_times[pred])

    model.Minimize(makespan)

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print("Optimal Task Schedule:")
        for i in range(num_tasks):
            print(f"Task {i + 1}: Start Time = {solver.Value(start_times[i])}, "
                  f"End Time = {solver.Value(end_times[i])}")
        print(f"Total Project Duration: {solver.Value(makespan)} hours")
    else:
        print('No solution found')


solve_task_scheduling()