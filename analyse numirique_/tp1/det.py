#import numpy as np

#def det(matrix):    
#    det = np.linalg.det(matrix)
#    return det

#def SME(A, b):
#    try:
#        A_inv = np.linalg.inv(A)
#    except np.linalg.LinAlgError:
#        return None
#    x = np.dot(A_inv, b)
#    return

N = 3 
B = [[0 for j in range(3)]] 


M = [[0 for j in range(N)] for i in range(N)]


def LireMatrice(N, M):
    for i in range(0, N):
        for j in range(0, N):
            M[i][j] = int(input('donner lelement: '))


def LireMatriceB():
    for j in range(3):
        B[0][j] = int(input(f'donner lelement:'))


def AfficherMatrice(N, M):
    for i in range(0, N):
        for j in range(0, N):
            if j == N - 1:
                print(M[i][j])
            else:
                print(M[i][j], end=" ")
    print("_" * (N * 2))  

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


def Comatrice(M, i, j):
    N = len(M)
    minor = [[M[x][y] for y in range(N) if y != j] for x in range(N) if x != i]
    return Determinant(len(minor), minor)

def Inverse(N, M):
    det = Determinant(N, M)
    
    comatrice = [[Comatrice(M, i, j) for j in range(N)] for i in range(N)]
    comatrice_transpose = [[comatrice[j][i] for j in range(N)] for i in range(N)]
    inverse = [[comatrice_transpose[i][j] / det for j in range(N)] for i in range(N)]
    return inverse
    
def ResoudreEquationMatricielle(A, B):
    N = len(A)
    inverse_A = Inverse(N, A)
    
    X = [[sum(inverse_A[i][k] * B[0][k] for k in range(len(B[0]))) for j in range(1)] 	for i in range(N)]
    return X

def AfficherResultMatrix(X):
    print("resultat AX = B:")
    for i in range(len(X)):
        print(X[i][0])  
    print("_" * 10)  

def AfficherMatriceB(B):
    print("Matrice B:")
    for j in range(3):
        if j == 2:
            print(B[0][j])
        else:
            print(B[0][j], end=" ")
    print("_" * 6)  


def AfficherResultMatrix(X):
    print("resultat AX = B:")
    for i in range(len(X)):
        print(X[i][0])  
    print("_" * 10)  




print("Lecture de la matrice A:")
LireMatrice(N, M)
AfficherMatrice(N, M)

print("Lecture de la matrice B:")
LireMatriceB()
AfficherMatriceB(B)

result_matrix = ResoudreEquationMatricielle(M, B)
AfficherResultMatrix(result_matrix) 

inverse_M = Inverse(N, M)
AfficherMatrice(N, inverse_M)
