myResearchSpace = {
    1: [(2, 2), (3, 1)],
    2: [(3, 4), (4, 3)],
    3: [(4, 2), (5, 1), (6, 13)],
    4: [(5, 5)],
    5: [(6, 10)],
    6: [],
}

heuristique = {
    1: 6,
    2: 5,
    3: 4,
    4: 2,
    5: 1,
    6: 0
}


class Node:
    def __init__(self, name, parent, cout, action):
        self.name = name
        self.parent = parent
        self.cout = cout
        self.action = action
        
class Node1:
    def __init__(self, name, parent, cout, coutf, action):
        self.name = name
        self.parent = parent
        self.cout = cout
        self.coutf = coutf
        self.action = action
        

def gener_successur(etat):
    if etat.name in myResearchSpace:
        listSucc = myResearchSpace[etat.name]
        if len(listSucc) > 0:
            return [Node(succ[0], etat, etat.cout + succ[1], "") for succ in listSucc]


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

def ucs_search(I, F):
    open = []
    closed = []
    ordreVisite = []
    open.append(Node(I, None, 0, ""))
    
    
    def sort_by_cout(node):
        return node.cout

    while open:
        open.sort(key=sort_by_cout)  
        N = open.pop(0)
        ordreVisite.append(N.name)
        
        if test_etat_final(N, F):
            return True, ordreVisite, getSolution(N), N.cout
        closed.append(N)
        successeurs = gener_successur(N)
        for succ in successeurs:
            if succ.name not in [x.name for x in closed]:
                if succ.name not in [x.name for x in open] or succ.cout < min([x.cout for x in open if x.name == succ.name]):
                    open.append(succ)
    return False, ordreVisite, [], 0


def gener_successur_astar(etat, heuristique):
    if etat.name in myResearchSpace:
        listSucc = myResearchSpace[etat.name]
        if len(listSucc) > 0:
            return [
                Node1(succ[0], etat, etat.cout + succ[1], etat.cout + succ[1] + heuristique[succ[0]], "") 
                for succ in listSucc
            ]
    

def astar_search(I, F, heuristique):
    open = []
    closed = []
    ordreVisite = []
    open.append(Node1(I, None, 0, heuristique[I], ""))
    
    
    def sort_by_coutf(node):
        return node.coutf

    while open:
        open.sort(key=sort_by_coutf) 
        N = open.pop(0)
        ordreVisite.append(N.name)
        
        if test_etat_final(N, F):
            return True, ordreVisite, getSolution(N), N.cout
        
        closed.append(N)
        successeurs = gener_successur_astar(N, heuristique)
        for succ in successeurs:
            if succ.name not in [x.name for x in closed]:
                if succ.name not in [x.name for x in open] or succ.coutf < min([x.coutf for x in open if x.name == succ.name]):
                    open.append(succ)
    return False, ordreVisite, [], 0


print ("===========================================")
result, ordreVisite, solution, coutSolution = ucs_search(1, [6])
print("Solution trouvée:", result)
print("Ordre de visite:", ordreVisite)
print("Solution:", solution)
print("Coût de la solution:", coutSolution)

print ("===========================================")
result, ordreVisite, solution, coutSolution = astar_search(1, [6], heuristique)
print("Solution trouvée:", result)
print("Ordre de visite:", ordreVisite)
print("Solution:", solution)
print("Coût de la solution:", coutSolution)
