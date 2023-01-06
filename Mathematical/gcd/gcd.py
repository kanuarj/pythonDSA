def gcd (a, b):
    if b == 0:
        return a

    rem = a % b
    return gcd (b, rem)

if __name__ == '__main__':
    print (gcd (899, 493))