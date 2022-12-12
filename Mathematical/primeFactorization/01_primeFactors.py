# Efficient program to print all prime factors of a given number

# Basic Approach:
# 1) While n is divisible by 2, print 2 and divide n by 2. 
# 2) After step 1, n must be odd. Now start a loop from i = 3 to the square root of n. While i divides n, print i, and divide n by i.
#     After i fails to divide n, increment i by 2 and continue. 
# 3) If n is a prime number and is greater than 2, then n will not become 1 by the above two steps. So print n if it is greater than 2. 

import math

def primeFactors (n):
    while n % 2 == 0:
        print (2)
        n /= 2

    for i in range (3, int (math.sqrt (n)) + 1, 2):
        while n % i == 0:
            print (i)
            n /= i

    if n > 2:
        print (n)

# Time Complexity: O(sqrt(n))
# In the worst case ( when either n or sqrt(n) is prime, for example: take n=11 or n=121 for both the cases for loop runs sqrt(n) times), the for loop runs for sqrt(n) times.
# The more number of times the while loop iterates on a number it reduces the original n, which also reduces the value of sqrt(n).
# Although the best case time complexity is O(log(n)), when the prime factors of n is only 2 and 3 or n is of the form (2^x*(3^y) where x>=0 and y>=0.

# Auxiliary Space: O(1)

if __name__ == '__main__':
    n = 315
    primeFactors (n)