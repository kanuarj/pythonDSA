from math import sqrt

# Naive Approach: A naive solution is to iterate through all numbers from 2 to sqrt(n) and for every number check if it divides n.
# If we find any number that divides, we return false.

def isPrimeNaiveApproach (n):
    if n <= 1:
        return False

    for i in range (2, int(sqrt(n))+1):
        if (n % i == 0):
            return False
    
    return True

# Time Complexity: O(sqrt(n))
# Auxiliary space: O(1)
# =================================================================================================================================
# Efficient Approach 
def isPrimeEfficientApproach (n):
    if n <= 1:
        return False
    
    if n == 2 or n == 3:
        return True

    if n % 2 is 0 or n % 3 == 0:
        return False

    for i in range (5, int(sqrt(n)), 6):
        if n % i is 0 or n % (i+2) is 0:
            return False

    return True

# Time complexity: O(sqrt(n))
# Auxiliary space: O(1)
# ==============================================================================================================================
# Recursive Approach 
def isPrimeRecursive (n, i):
    if n is 0 or n is 1:
        return False

    if n is i:
        return True

    if n % i == 0:
        return False

    i += 1
    return isPrimeRecursive (n, i)

def isPrimeRecursiveWrapper (n):
    return isPrimeRecursive (n, 2)

# Time Complexity: O(N)
# Auxiliary Space: O(N) 

if __name__ == '__main__':
    # print (isPrimeNaiveApproach (4))
    # print (isPrimeEfficientApproach (11))
    print (isPrimeRecursiveWrapper(5))