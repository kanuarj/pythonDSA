def factorialRecursive (n):
    if n == 0:
        return 1
    
    return n * factorialRecursive (n-1)

# Time Complexity: O(n)
# Auxiliary Space: O(n)

if __name__ == '__main__':
    print (factorialRecursive (5))