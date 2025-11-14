# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 10:10:16 2024

@author: Tiho_GHL
"""
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
    def __init__(self, name, parent , action):
        self.name = name #Le nom de l'etat
        self.parent = parent # Le père d'un nœud
        self.action = action # L'action qui génére le nœud (optionel)
        
        
def gener_successur(etat):
    if etat.name in myResearchSpace:
       listSucc=myResearchSpace[etat.name]
       if len(listSucc) > 0:
          return [Node(x,etat,"") for x in listSucc]
       else:
           return []
       
def test_etat_final(C,F):
     if C.name in F:
        return True
     else: 
         return False      
    
    
def getSolution(N):
    solution=[]
    parent=N.parent
    if parent is not None: solution=[parent.name,N.name]
    else: return [N.name]
    while parent.parent:
        solution.insert(0,parent.parent.name)
        parent=parent.parent
    return solution

# Fonction DLS Search (Depth-Limited Search)
def dls_search(I, F, L, OV):
    OV.append(I.name)  
    if test_etat_final(I, F):  
        return True, OV, getSolution(I)
    elif L == 0: 
        return False, OV, []
    else:
        for succ in gener_successur(I):
            found, OV, path = dls_search(succ, F, L - 1, OV)
            if found:
                return True, OV, path
        return False, OV, []

def IDS_search(I, F):
    limit = 0
    while True:
        OV = []
        found, OV, path = dls_search(I, F, limit, OV)
        if found:
            return True, OV, path
        if limit > len(OV):
            break
        limit += 1
    return False, OV, []

    
    
print("=======DLS_SEARCH==========\n")
I=Node(1,None,"")
print(dls_search(I,[1],0,[])) 
print(dls_search(I,[10],0,[]))
print(dls_search(I,[10],1,[]))
print(dls_search(I,[10],2,[])) 
print(dls_search(I,[10],3,[]))
print(dls_search(I,[11],4,[]))

print("=======IDS_SEARCH==========\n")
#I=Node(1,None,"")
print(IDS_search(I,[1]))
print(IDS_search(I,[7]))
print(IDS_search(I,[8]))
print(IDS_search(I,[10]))
print(IDS_search(I,[11]))