def recursiveLCS (X, Y, charOfX, charOfY):
    if charOfX == 0 or charOfY == 0:
        return 0
    elif X[charOfX-1] == Y[charOfY-1]:
        return 1 + recursiveLCS (X, Y, charOfX-1, charOfY-1)
    else:
        return max (recursiveLCS (X, Y, charOfX-1, charOfY), recursiveLCS (X, Y, charOfX, charOfY-1))

def memoizationLCS (X, Y, m, n, memoi):
    if m == 0 or n == 0:
        return 0
    if (memoi[m][n] is not -1):
        return memoi[m][n]
    if X[m-1] == Y[n-1]:
        memoi[m][n] = 1 + memoizationLCS (X, Y, m-1, n-1, memoi)
        return memoi[m][n]
    
    memoi[m][n] = max (memoizationLCS (X, Y, m-1, n, memoi), memoizationLCS (X, Y, m, n-1, memoi))
    return memoi[m][n]

def LCSDP (X, Y):
    m, n = len (X), len (Y)
    L = [[None]*(n+1) for _ in range (m+1)]
    for i in range (m+1):
        for j in range (n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = 1 + L[i-1][j-1]
            else:
                L[i][j] = max (L[i-1][j], L[i][j-1])

    return L[m][n]            

if __name__ == '__main__':
    X = 'CGATAATTGAGA'
    Y = 'GTTCCTAATA'
    memoi = [[-1 for _ in range(len(Y)+1)] for _ in range(len(X)+1)]
    # print (recursiveLCS (X, Y, len(X), len(Y)))
    # print (memoizationLCS (X, Y, len(X), len(Y), memoi))
    print (LCSDP (X, Y))
