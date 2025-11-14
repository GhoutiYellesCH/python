from collections import deque

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
Open = []
Closed = []
files = deque() 

class Node:
 	def __init__(self, name, parent):
 		self.name = name 
 		self.parent = parent 
 		
def dfs_search(I,F):
 	open=[]
 	closed=[]
 	ordreVisite=[]
 	open.append(Node(I, None))
 	while open:
 		N = open.pop()
 		ordreVisite.append(N.name)
 		if test_etat_final(F, N):
 			return True,ordreVisite,getSolution(N)
 		else:
 			closed.append(N)
 			succ = genere_successeur(N.name)
 			print(succ)
 			if len(succ) > 0:
 				for s in succ:
 					if s.name not in [x.name for x in open] and s.name not in [x.name for x in closed]:
 						open.append(s)
 	return False,ordreVisite,[]

def genere_successeur(node):
	return myResearchSpace.get(node)
	
def test_etat_final(list_final, etat):
	if etat in list_final:
		return True
	return False

def BFS():
	print("BFS")
	while Open :
		i = Open.pop()
		Closed.append(i)
		print(f"etat depiler : {i}")
		tmp = genere_successeur(i)
		for e1 in tmp :
			if e1 in  Open or Closed:
				Open.append(e1)
				
def search(list_final, I):
	print("search")
	Open.append(I)
	while Open :
		i = Open.pop()
		Closed.append(i)
		print(f"etat depiler : {i}")
		tmp = genere_successeur(i)
		for e1 in tmp :
			if e1 in  Open or Closed:
				Open.append(e1)
			if test_etat_final(list_final, e1):
				return True
	return False
		
def DFS():
	print("DFS")
	files.append(1)
	while files :
		i = files.popleft()
		Closed.append(i)
		print(f"etat depiler : {i}")
		tmp = genere_successeur(i)
		for e1 in tmp :
			if e1 in  files or Closed:
				files.append(e1)
				
def search2(list_final, I):
	print("search2")
	files.append(I)
	while files :
		i = files.popleft()
		Closed.append(i)
		print(f"etat depiler : {i}")
		tmp = genere_successeur(i)
		for e1 in tmp :
			if e1 in  files or Closed:
				files.append(e1)
			if test_etat_final(list_final, e1):
				return True
	return False
			
def main():
	#etat_finaux = [8,9,10,5,7]
	etat_finaux = [9]
	Open.append(1)
	BFS()
	DFS()
	I = int(input("donner l'etat initial "))
	print(search(etat_finaux , I))
	print(search2(etat_finaux , I))
	print("poo part")
	dfs_search(I,etat_finaux )
	
	
main()
