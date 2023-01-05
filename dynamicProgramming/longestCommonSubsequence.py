def recursiveLCS (X, Y, charOfX, charOfY):
    if charOfX == 0 or charOfY == 0:
        return 0
    elif X[charOfX-1] == Y[charOfY-1]:
        return 1 + recursiveLCS (X, Y, charOfX-1, charOfY-1)
    else:
        return max (recursiveLCS (X, Y, charOfX-1, charOfY), recursiveLCS (X, Y, charOfX, charOfY-1))

if __name__ == '__main__':
    X = 'CGATAATTGAGA'
    Y = 'GTTCCTAATA'
    print (recursiveLCS (X, Y, len(X), len(Y)))
