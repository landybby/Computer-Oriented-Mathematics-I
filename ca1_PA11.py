def matrixbilden(A):
    a = [[int(x) for x in b.split(" ")] for b in A.split(", ")]
    return a 

def matrixzustring(a):
    b = ""
    for i in range(len(a)):
        b += str(a[i][0])
        if len(a[i]) > 1:
            for j in range(1, len(a[i])):
                b = b + " " + str(a[i][j])
        if i != len(a) - 1:
            b = b + ", "
    return b

def LU_decomposition(M):
    u = matrixbilden(M)
    n = len(u)
    l = [[0 for i in range(n)] for x in range(n)]
    for i in range(n-1):
        for j in range(i,n-1):
            if u[j+1][i] == 0:
                continue
            else:
                a = u[j+1][i] / u[i][i] 
                for x in range(n):
                    u[j+1][x] = int(u[j+1][x] - a*u[i][x])
                l[j+1][i] = int(a)
    for i in range(n-1):
        for j in range(i,n-1):
            if l[j+1][i] != 0:
                u[j+1][i] = l[j+1][i]
    u = matrixzustring(u)
    return u