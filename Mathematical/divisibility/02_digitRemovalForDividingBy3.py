# Number of digits to be removed to make a number divisible by 3

# Given a very large number num (1 <= num <= 10^1000), print the number of digits that needs to be removed to make the number exactly divisible by 3.
# If it is not possible then print -1.

# Examples : 
# Input: num = "1234"
# Output: 1
# Explanation: we need to remove one 
# digit that is 1 or 4, to make the
# number divisible by 3.on 

# Input: num = "11"
# Output: -1
# Explanation: It is not possible to 
# remove any digits and make it divisible
# by 3.
# ===========================================================
# The idea is based on the fact that a number is multiple of 3 if and only if sum of its digits is multiple of 3 (See this for details).
# One important observation used here is that the answer is at most 2 if an answer exists. So here are the only options for the function: 

#   Sum of digits is already equal to 0 modulo 3. Thus, we don’t have to erase any digits.
#   There exists such a digit that equals sum modulo 3. Then we just have to erase a single digit
#   All the digits are neither divisible by 3 nor equal to sum modulo 3. So two of such digits will sum up to number,
#     which equals sum modulo 3, (2+2) mod 3=1, (1+1) mod 3=2

def removalForDivisible (num):
    n = len (num)
    sum = 0
    for i in range (n):
        sum += int(num[i])

    if sum % 3 == 0:
        return 0

    if n is 1 or n is 2:
        return -1
    
    for j in range (n):
        if sum % 3 == int (num[j]) % 3:
            return 1
        
    return 2

# Time Complexity: O(N), as we are using a loop to traverse N times.
# Auxiliary Space: O(1), as we are not using any extra space.

if __name__ == '__main__':
    outcome = removalForDivisible ('9124')
    print (outcome)
