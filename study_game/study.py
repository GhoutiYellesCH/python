import os
import time as tm

data_ai = { 
# copyright for univ 
"1": "Belabed Amine"
"2": "Université De Tlemcen – Faculté des sciences, Département Informatique"
"3": "2024-2025"

# chapter one 
"chpter_1": "La résolution des problèmes par la recherche" 
# table de contenu
"intro" : "Introduction"
#Comment définir un problème ?

# example
"ex1" : "les jeux, planification , la preuve de théorèmes ,· · ·"

# contenu 
#La démarche d’IA :
#▶ L’algorithme doit être "neutre" sur le domaine concerné
#▶ Les connaissances de description du problème et de sa résolution doivent être clairement séparés de l’algorithme.


#Comment définir un problème ?
#Un problème peut être définit par 5 composants :
#1 Définir l’espace des états.
#2 Définir l’état initial : l’état de départ ;
#3 Définir les opérateurs
#▶ Fonction successeur : permettant de retourner l’ensemble des états atteignables par une action particulière.
#▶ L’état initial + l’ensemble des états atteignables : l’espace des états.
#▶ Un chemin dans l’espace des états est une séquence d’états connectés par une séquence d’actions (opérations).
#4 Une fonction de test :permettant de savoir que la solution est trouvée.
#5 Une fonction de coût :Associe un coût au chemin de la solution.
#▶ Une solution optimale est une solution qui minimise la fonction de coût.


# definition 
"def_p": "Un problème :"
"def_pc": "une situation devant laquelle on ne voit pas directement les étapes permettant de dépasser la situation et obtenir la solution."

"RSP" : "Résoudre un problème :"
"RSPc": "revient à chercher un chemin qui mène d’une situation initiale à une autre finale pour atteindre un but."

#xemple : Le jeu de taquin
"" : """
|--|--|--|		|--|--|--|
|  |  |  |		|  |  |  |
|--|--|--|		|--|--|--|
|  |  |  |		|  |  |  |
|--|--|--|		|--|--|--|
|  |  |  |		|  |  |  |
|--|--|--|		|--|--|--|
 """
 } 
 
data_pl = { 
1: "" 
2: ""
3: ""
 } 
 
data_an = { 
1: "" 
2: ""
3: ""
 } 

data_bdd = { 
1: "" 
2: ""
3: ""
 } 

data_os = { 
1: "" 
2: ""
3: ""
 } 
 
data_gl = { 
1: "" 
2: ""
3: ""
 }  
 
data_md = { 
1: "" 
2: ""
3: "   "
 } 

# here the ai module 

def AI(op):
	try:
		op2 = 
		if op == 1:
			op = select_chapter()
			if op == 1:
				ai_quize(op)
			elif op == 2:
				ai_quize(op)
		elif op == 2:
			op = select_chapter()
			if op == 1:
				ai_read(op)
			elif op == 2:
				ai_read(op)
		else :
			op = select_chapter()
			if op == 1:
				ai_write(op)
			elif op == 2:
				ai_write(op)
		start_over()
	except KeyboardInterrupt :
		os.system("clear")
		print(" CTR + C was press ")
		tm.sleep(0.5)

def ai_quize(op)

# here the pl module 
	
def PL():
	try:
		if op == 1:
			print(" quiz PL here")
		elif op == 2:
			print("read PL here")
		else :
			print("write PL here")
		start_over()
	except KeyboardInterrupt :
		os.system("clear")
		print(" CTR + C was press ")
		tm.sleep(0.5)

# here the AN module 

def AN():
	try:
		if op == 1:
			print(" quiz AN here")
		elif op == 2:
			print("read AN here")
		else :
			print("write AN here")
		start_over()
	except KeyboardInterrupt :
		os.system("clear")
		print(" CTR + C was press ")
		tm.sleep(0.5)
	
# here the BDD module 
	
def BDD():
	try:
		if op == 1:
			print(" quiz BDD here")
		elif op == 2:
			print("read BDD here")
		else :
			print("write BDD here")
		start_over()
	except KeyboardInterrupt :
		os.system("clear")
		print(" CTR + C was press ")
		tm.sleep(0.5)

# here the OS module 	

def OS():
	try:
		if op == 1:
			print(" quiz OS here")
		elif op == 2:
			print("read OS here")
		else :
			print("write OS here")
		start_over()
	except KeyboardInterrupt :
		os.system("clear")
		print(" CTR + C was press ")
		tm.sleep(0.5)

# here the GL module 

def GL():
	try:
		if op == 1:
			print(" quiz GL here")
		elif op == 2:
			print("read GL here")
		else :
			print("write GL here")
		start_over()
	except KeyboardInterrupt :
		os.system("clear")
		print(" CTR + C was press ")
		tm.sleep(0.5)
	
# here the MD module 
	
def MD():
	try:
		if op == 1:
			print(" quiz MD here")
		elif op == 2:
			print("read MD here")
		else :
			print("write MD here") 
		start_over()
	except KeyboardInterrupt :
		os.system("clear")
		print(" CTR + C was press ")
		tm.sleep(0.5)
		
# system conrtol panel

def select_chapter():
	try:
		print(" chose the chapter")
		print(" op 1 = chapter I ")
		print(" op 2 = chapter II ")
		while True:
			if op == 1:
				return 1			
			elif op == 2:
				return 2
			else :
				print("no chapter selected") 
	except KeyboardInterrupt :
		os.system("clear")
		print(" CTR + C was press ")
		tm.sleep(0.5)


def start_over():
	print("")
	print("do you want to start over")
	choice = input("y / ... ")
	if choice == "y":
		main()
	else :
		return
		
def menu():
	try:
		print("")
		print(
		"""
		0- to exit from menu
1- intiligence artificial  	4- advance database 
2- programmation lininere	5- operating system 
3- analyse numirique		6- software inginering 
		7- mobile development 
		""")
	
		while True:
			choice = int(input("the number : "))
			if choice == 0:
				return 0
			elif choice == 1:
				return 1
			elif choice == 2:
				return 2
			elif choice == 3:
				return 3
			elif choice == 4:
				return 4
			elif choice == 5:
				return 5
			elif choice == 6:
				return 6
			elif choice == 7:
				return 7 
			else :
				print("enter another number")
	except KeyboardInterrupt :
		os.system("clear")
		print(" CTR + C was press ")
		tm.sleep(1)
		return

def option():
	try:
		print(" chose an option ")
		print(" 1 - Quiz - ")
		print(" 2 - Read - ")
		print(" 3 - Write - ")
		return int(input("tap here : ")) 
	except KeyboardInterrupt :
		os.system("clear")
		print(" CTR + C was press ")
		tm.sleep(0.5)
		return


def main():
	try :
		os.system("clear")
		print(" start from here ")
		op = option()
		choice = menu()
		if choice == 0:
			return
		elif choice == 1:
			AI(op)
		elif choice == 2:
			PL(op)
		elif choice == 3:
			AN(op)
		elif choice == 4:
			BDD(op)
		elif choice == 5:
			OS(op)
		elif choice == 6:
			GL(op)
		else:
			MD(op)
	except KeyboardInterrupt :
		os.system("clear")
		print(" CTR + C was press ")
		tm.sleep(0.5)
		
main()

# makig a timing and progress bar 
# making function to speed up the progress bar 
# [x] update the main programm by add chose mode -- quiz -- write -- read only -- 
