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

if __name__ == '__main__':
    n = 9
    # print (fiboRecursive (n))
    print (fiboDynamic(n))