def factorialRecursive (n):
    if n == 0:
        return 1
    
    return n * factorialRecursive (n-1)

# Time Complexity: O(n)
# Auxiliary Space: O(n)

def factorialAnotherApproach (n):
    if n is 0:
        return 1
    
    i, factorial = n, 1

    while (n/i) != n:
        factorial *= i
        i -= 1

    return factorial

# Time complexity: O(N)
# Auxiliary Space: O(1)

if __name__ == '__main__':
    # print (factorialRecursive (5))
    print (factorialAnotherApproach (5))