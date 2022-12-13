# Sieve of Eratosthenes
# Given a number n, print all primes smaller than or equal to n. It is also given that n is a small number. 

# Example: 
# Input : n =10
# Output : 2 3 5 7 

# Input : n = 20 
# Output: 2 3 5 7 11 13 17 19

def sieveOfEratosthenes (n):
    primeHolder = [True for x in range (n+1)]
    i = 2
    while (i*i <= n):
        if primeHolder[i] == True:
            for k in range (i*i, n+1, i):
                primeHolder[k] = False
        i += 1

    for j in range (2, n+1):
        if primeHolder[j]:
            print (j, end = ' ')

# Time Complexity: O(n*log(log(n)))
# Auxiliary Space: O(n)

if __name__ == '__main__':
    sieveOfEratosthenes (50)