# Use Recursion as most basic method
def fiboRecursive (n):
    if n <= 1:
        return n
    return fiboRecursive (n-1) + fiboRecursive (n-2)
# Time Complexity: Exponential, as every function calls two other functions.
# =========================================================================================
# Using Dynamic Programming to avoid the exponential time complexity
def fiboDynamic (n):
    holder = [0, 1]
    for i in range (2, n+1):
        holder.append (holder[i-1] + holder[i-2])
    return holder[n]
# Time complexity: O(n) for given n
# Auxiliary space: O(n)
# ===========================================================================================
# Space Optimized Method
def fiboSpaceOptimized (n):
    a, b = 0, 1
    if n < 0:
        return -1
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range (2, n+1):
            c = a + b
            a = b
            b = c
        return b
# Time Complexity: O(n) 
# Extra Space: O(1)

if __name__ == '__main__':
    n = 9
    # print (fiboRecursive (n))
    # print (fiboDynamic(n))
    print (fiboSpaceOptimized (n))