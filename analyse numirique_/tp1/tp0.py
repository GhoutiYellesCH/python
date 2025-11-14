def readMat(T, n):
    for i in range(0, n):
        for j in range(0, n):
            T[i][j] = input("T[%d][%d]= " % (i, j))


def readMatNC(T, n, m):
    for i in range(0, n):
        for j in range(0, m):
            T[i][j] = int(input("T[%d][%d]= " % (i, j)))


def writeMat(T, n):
    for i in range(0, n):
        print("\n")
        for j in range(0, n):
            print("T[%d][%d]= " % (i, j), T[i][j], end="\t")
    print("\n")


def writeMatNC(T, n, m):
    for i in range(0, n):
        print("\n")
        for j in range(0, m):
            print("T[%d][%d]= " % (i, j), T[i][j], end="\t")


def identity(n):
    for i in range(0, n):
        print("\n")
        for j in range(0, n):
            if i == j:
                print("T[%d][%d]= " % (i, j), 1, end="\t")
            else:
                print("T[%d][%d]= " % (i, j), 0, end="\t")


def sommeMat(T1, T2, n, m):
    s = [[0 for i in range(0, m)] for j in range(0, n)]
    for i in range(0, n):
        for j in range(0, m):
            s[i][j] = T1[i][j] + T2[i][j]

    writeMatNC(s, n, m)


def produitMat(T1, T2, l1, m, c2):
    p = [[0 for i in range(0, l1)] for j in range(0, m)]
    for i in range(0, l1):
        for j in range(0, m):
            for k in range(0, c2):
                p[j][i] += T1[i][k] * T2[k][j]
    writeMatNC(p, m, l1)


def transpose(T, n):
    t = 0
    for i in range(0, int(n/2)):
        for j in range(0, int(n/2)):
            t = T[i][j]
            T[i][j] = T[j][i]
            T[j][i] = t

    writeMat(T, n)
    for i in range(0, n):
        for j in range(0, n):
            t = T[i][j]
            T[i][j] = T[i][n - 1 - j]
            T[i][n - 1 - j] = T

    writeMat(T, n)


def q1_2():
    n = int(input("Enter the size: "))
    T = [[0 for i in range(0, n)] for j in range(0, n)]
    readMat(T, n)
    writeMat(T, n)


def q3():
    n = int(input("Enter the size of the identity matrix: "))
    identity(n)


def q4():
    n = int(input("Enter the number of rows: "))
    m = int(input("Enter the number of columns: "))
    T1 = [[0 for i in range(0, m)] for j in range(0, n)]
    T2 = [[0 for i in range(0, m)] for j in range(0, n)]
    readMatNC(T1, n, m)
    writeMatNC(T1, n, m)
    readMatNC(T2, n, m)
    writeMatNC(T2, n, m)
    sommeMat(T1, T2, n, m)


def q5():
    n1 = int(input("Enter the number of rows of T1: "))
    m1 = int(input("Enter the number of columns of T1: "))
    n2 = int(input("Enter the number of rows of T2: "))
    m2 = int(input("Enter the number of columns of T2: "))
    T1 = [[0 for i in range(0, m1)] for j in range(0, n1)]
    T2 = [[0 for i in range(0, m2)] for j in range(0, n2)]

    if m1 != n2:
        print(
            "Impossible because the number of columns of T1 %d is not equal to the number of rows of T2 %d " % (m1, n2))
    else:
        readMatNC(T1, n1, m1)
        writeMatNC(T1, n1, m1)
        readMatNC(T2, n2, m2)
        writeMatNC(T2, n2, m2)
        produitMat(T1, T2, n1, m1, m2)


def q6():
    n = int(input("Enter the size: "))
    T = [[0 for i in range(0, n)] for j in range(0, n)]
    readMat(T, n)
    writeMat(T, n)
    transpose(T, n)


q6()

m = input()
