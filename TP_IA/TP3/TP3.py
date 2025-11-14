myResearchSpace={
 1:[2, 3],
 2:[4, 5],
 3:[6, 7],
 4:[8],
 5:[],
 6:[9, 10],
 7:[],
 8:[],
 9:[],
 10:[],
}

class Node:
    def __init__(self, name, parent, action):
        self.name = name
        self.parent = parent
        self.action = action

def gener_successur(etat):
    if etat.name in myResearchSpace:
        listSucc = myResearchSpace[etat.name]
        if len(listSucc) > 0:
            return [Node(x, etat, "") for x in listSucc]
        else:
            return []
    else:
        return []

def test_etat_final(C, F):
    return C.name in F

def getSolution(N):
    solution = []
    parent = N.parent
    if parent is not None:
        solution = [parent.name, N.name]
    else:
        return [N.name]
    while parent.parent:
        solution.insert(0, parent.parent.name)
        parent = parent.parent
    return solution

def dls_search1(I, F, L, OV):
    OV.append(I.name)
    if test_etat_final(I, F):
        return True, OV, getSolution(I)
    if L == 0:
        return False, OV, []
    successeurs = gener_successur(I)
    for succ in successeurs:
        if succ.name not in OV:
            trouvé, OV, solution = dls_search1(succ, F, L-1, OV)
            if trouvé:
                return True, OV, solution
    return False, OV, []

I = Node(1, None, "")
print(dls_search1(I, [1], 0, []))
print(dls_search1(I, [10], 0, []))
print(dls_search1(I, [10], 1, []))
print(dls_search1(I, [10], 2, []))
print(dls_search1(I, [10], 3, []))
print(dls_search1(I, [11], 4, []))

