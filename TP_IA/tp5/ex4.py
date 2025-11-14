from ortools.sat.python import cp_model


def solve_knapsack_problem():

    values = [
        360,
        83,
        59,
        130,
        431,
        67,
        230,
        52,
        93,
        125,
        670,
        892,
        600,
        38,
        48,
        147,
        78,
        256,
        63,
        17,
        120,
        164,
        432,
        35,
        92,
        110,
        22,
        42,
        50,
        323,
        514,
        28,
        87,
        73,
        78,
        15,
        26,
        78,
        210,
        36,
        85,
        189,
        274,
        43,
        33,
        10,
        19,
        389,
        276,
        312,
    ]

    weights = [
        7,
        1,
        30,
        22,
        80,
        94,
        11,
        81,
        70,
        64,
        59,
        18,
        1,
        36,
        3,
        8,
        15,
        42,
        9,
        1,
        42,
        47,
        52,
        32,
        26,
        48,
        55,
        6,
        29,
        84,
        2,
        4,
        18,
        56,
        7,
        29,
        93,
        44,
        71,
        3,
        86,
        66,
        31,
        65,
        1,
        79,
        20,
        65,
        52,
        13,
    ]

    max_weight = 850
    num_items = len(values)
    # value

    model = cp_model.CpModel()

    # - Les variables : X={O1, O2, O,3 O4}.
    # - Les domaines : D(O1)=D(O2)=D(O3)=D(O4)={0.1}
    items = [model.NewIntVar(0, 1, f"item_{i}") for i in range(num_items)]

    model.Add(cp_model.LinearExpr.WeightedSum(items, weights) <= max_weight)
    # 5*O1+ 10*O2+ 15*O3+ 8*O4 < Pmax.

    model.Maximize(cp_model.LinearExpr.WeightedSum(items, values))
    #

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        selected_items = [i for i in range(num_items) if solver.Value(items[i]) == 1]
        total_value = sum(values[i] for i in selected_items)
        total_weight = sum(weights[i] for i in selected_items)

        print("Selected Items Indices:", selected_items)
        print("Total Value:", total_value)
        print("Total Weight:", total_weight)
    else:
        print("No solution found")


solve_knapsack_problem()

