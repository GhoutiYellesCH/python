def LireMatrice(N,M):
    for i in range(0,N):
        for j in range(0,N):
            M[i][j] = int(input('donner lelement: '))

    for i in range(N):

        if i != N-1:

            print("_", end = " ")

        else:
            print("_")

def AfficherMatrice(N,M):
    for i in range(0,N):
        for j in range(0,N):
            if j == N-1:
                print(M[i][j])
            else:
                print(M[i][j], end = " ")
    for i in range(N):
        if i != N-1:
            print("_", end = " ")
        else:
            print("_")
            
def LireMatriceB(k, B):
    for j in range(k):
        B[0][j] = int(input(f'donner lelement:'))


def AfficherMatrice(N, M):
    for i in range(0, N):
        for j in range(0, N):
            if j == N - 1:
                print(M[i][j])
            else:
                print(M[i][j], end=" ")
    print("_" * (N * 2)) 

def MatriceDidentite(N):
    for i in range(0,N):
        for j in range(0,N):
            if (j == i) and (j == N-1):
                print(1)
            elif (j != i ) and (j == N-1):
                print(0)
            elif (j==i):
                print(1, end = " ")
            else:
                print(0, end = " ")

def SommeDeMatrice(N,M,M2):
    for i in range(0,N):
        for j in range(0,N):
            M[i][j] += M2[i][j]

def ProduitDeMatrice(N, M, M2):
    MM = [[0 for i in range(N)] for j in range(N)]  

    for i in range(N):  
        for j in range(N):  
            for k in range(N):  
                MM[i][j] += M[i][k] * M2[k][j]
    
    return MM

def Transpose(N,M):
    MM = [[0 for i in range(N)] for j in range(N)]  

    for i in range(N):
        for j in range(N):
            MM[i][j] = M[j][i]
    return MM

def IsTriangulaireSup(N,M):
    for i in range(1, N):
        for j in range(i):
            if M[i][j] != 0:
                return False
    return True

def IsTriangulaireInf(N,M):
    for i in range(N):
        for j in range(i + 1, N):
            if M[i][j] != 0:
                return False
    return True

def IsDiagonale(N,M):
    if IsTriangulaireInf(N,M) and IsTriangulaireSup(N,M):
        return True
    else:
        return False
    
def IsSym(N,M):
    for i in range(N):
        for j in range(N):
            if M[i][j] != M [j][i]:
                return False
    return True
    
def Determinant(N, M): 
    if N == 1:
        return M[0][0]  
    elif N == 2:
        return M[0][0] * M[1][1] - M[0][1] * M[1][0]  
    det = 0
    for k in range(N):
        minor = [[M[i][j] for j in range(N) if j != k] for i in range(1, N)]
        det += ((-1) ** k) * M[0][k] * Determinant(N - 1, minor)
    return det


def Comatricecalc(M, i, j):
    N = len(M)
    minor = [[M[x][y] for y in range(N) if y != j] for x in range(N) if x != i]
    return Determinant(len(minor), minor)


def Inverse(N, M):
    det = Determinant(N, M)
    if det == 0:
        return None
    comatrice = [[Comatricecalc(M, i, j) for j in range(N)] for i in range(N)]
    comatrice_transpose = [[comatrice[j][i] for j in range(N)] for i in range(N)]
    inverse = [[comatrice_transpose[i][j] / det for j in range(N)] for i in range(N)]
    return inverse

def AfficherResultMatrix(X):
    print("resultat AX = B:")
    for i in range(len(X)):
        print(X[i][0])  
    print("_" * 10)  

def ResoudreEquationMatricielle(A, B):
    N = len(A)
    inverse_A = Inverse(N, A)
    n = len(A)
    if inverse_A is None:
        return None
    X = [[sum(inverse_A[i][k] * B[0][k] for k in range(len(B[0]))) for j in range(1)] 	for i in range(N)]
    return X

def secondmenu(N):
	print("==== Menu2 ====") 
	print("entrer la valeur de k pour la deuxieme matrice")
	k = int(input())
	
	B = [[0 for j in range(k)]] 
	M = [[0 for j in range(N)] for i in range(N)]

	print("Lecture de la matrice A:")
	LireMatrice(N, M)
	AfficherMatrice(N, M)

	print("Lecture de la matrice B:")
	LireMatriceB(k,B)
	#AfficherResultMatrix(B)
	
	print("l'equation matricielle")
	result_matrix = ResoudreEquationMatricielle(M, B)
	AfficherResultMatrix(result_matrix) 
	
	print("l'inverse")
	inverse_M = Inverse(N, M)
	AfficherMatrice(N, inverse_M)
	
def menu():
    print("==== Menu ====")
    print("1. Lire une matrice")
    print("2. Afficher une matrice")
    print("3. Afficher la matrice identité")
    print("4. Somme de deux matrices")
    print("5. Produit de deux matrices")
    print("6. Transposée d'une matrice")
    print("7. Tester si une matrice est triangulaire supérieure")
    print("8. Tester si une matrice est triangulaire inférieure")
    print("9. Tester si une matrice est diagonale")
    print("10. Tester si une matrice est symétrique")
    print("11. Le determinent")
    print("12. Calcule l'invers et Equation Matricielle matrice")
    print("0. Quitter")
    print("================")
    
def main():
    M = []
    M2 = []
    N = int(input("Donner la taille de la matrice carrée N: "))
    M = [[0 for _ in range(N)] for _ in range(N)]
    M2 = [[0 for _ in range(N)] for _ in range(N)]

    while True:
        menu()
        choix = int(input("Choisissez une option: "))
        
        if choix == 1:
            print("Lecture de la première matrice:")
            LireMatrice(N, M)
        elif choix == 2:
            print("Affichage de la matrice:")
            AfficherMatrice(N, M)
        elif choix == 3:
            print("Matrice identité:")
            MatriceDidentite(N)
        elif choix == 4:
            print("Lecture de la seconde matrice pour la somme:")
            LireMatrice(N, M2)
            SommeDeMatrice(N, M, M2)
            print("Résultat après somme:")
            AfficherMatrice(N, M)
        elif choix == 5:
            print("Lecture de la seconde matrice pour le produit:")
            LireMatrice(N, M2)
            M_result = ProduitDeMatrice(N, M, M2)
            print("Résultat du produit de matrices:")
            AfficherMatrice(N, M_result)
        elif choix == 6:
            M_transpose = Transpose(N, M)
            print("Matrice transposée:")
            AfficherMatrice(N, M_transpose)
        elif choix == 7:
            if IsTriangulaireSup(N, M):
                print("La matrice est triangulaire supérieure.")
            else:
                print("La matrice n'est pas triangulaire supérieure.")
        elif choix == 8:
            if IsTriangulaireInf(N, M):
                print("La matrice est triangulaire inférieure.")
            else:
                print("La matrice n'est pas triangulaire inférieure.")
        elif choix == 9:
            if IsDiagonale(N, M):
                print("La matrice est diagonale.")
            else:
                print("La matrice n'est pas diagonale.")
        elif choix == 10:
            if IsSym(N, M):
                print("La matrice est symétrique.")
            else:
                print("La matrice n'est pas symétrique.")
        elif choix == 11:
        	det = Determinant(N, M)
        	print(det)
        	
        elif choix == 12:
        	secondmenu(N)

        elif choix == 0:
            print("Au revoir!")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

main()

