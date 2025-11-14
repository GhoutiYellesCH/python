def MatriceInitiale(Mat,N,M):
    for i in range(0,N):
        print('\n')
        for j in range(0,M):
            Mat[i][j] = int(input(f'Mat[{i}][{j}]'))

def AfficherMatrice(Mat,N,M):
    for i in range(0,N):
        print('\n')
        for j in range(0,M):
                print(f"{Mat[i][j]}", end='\t')



def ChercherVariableEntrante(Mat,N,M):
    Zj = [0 for _ in range(M)]
    Zj[0] = 0
    CjZj = [0 for _ in range(M)]
    for i in range(0,N):
        for j in range(0,M):
            if i<4 & i<N & j<M:
                Zj[j] = Zj[j] + ( Mat[i+1][j+1] * Mat[i+1][0])
    for j in range(0, M):
        if j > 1:
            CjZj[j] = Mat[0][j] - Zj[j]
    max = CjZj[0]
    index = 0
    for j in range(0,M):
        if max < CjZj[j]:
            max = CjZj[j]
            index = j
    return index


def ChercherVariableSortante(Mat,N,index):
    Ration = [0 for _ in range(N)]
    for i in range(0,N):
        if i+1 <N:
            if Mat[i+1][index] !=0:
                Ration[i] = Mat[i+1][1] / Mat[i+1][index]
    min = Ration[0]
    index2 = 0
    for i in range(0,N):
        if min > Ration[i] and Ration[i] !=0:
            min = Ration[i]
            index2 = i+1
    return index2


N = int(input('nombre de lines: '))
M = int(input('nombre de colonnes: '))
Mat = [[0 for _ in range(M)] for _ in range(N)]
Mat = [[0,0,800,300,0,0,0],
       [0,400,2,1,1,0,0],
       [0,150,1,0,0,1,0],
       [0,200,0,1,0,0,1]]

#MatriceInitiale(Mat,N,M)
AfficherMatrice(Mat,N,M)
print()
Pline = ChercherVariableEntrante(Mat,N,M)
Pcol =  ChercherVariableSortante(Mat,N,Pline)
