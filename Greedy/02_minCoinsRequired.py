# Greedy Algorithm to find Minimum number of Coins
# Given a value of V Rs and an infinite supply of each of the denominations {1, 2, 5, 10, 20, 50, 100, 500, 1000} valued coins/notes,
# The task is to find the minimum number of coins and/or notes needed to make the change?
# Examples:  
# Input: V = 70
# Output: 2
# Explanation: We need a 50 Rs note and a 20 Rs note.

# Input: V = 121
# Output: 3
# Explanation: We need a 100 Rs note, a 20 Rs note, and a 1 Rs coin.

# Approach: 
# The intuition would be to take coins with greater value first.
# This can reduce the total number of coins needed.
# Start from the largest possible denomination and keep adding denominations while the remaining value is greater than 0. 

# Implementation : 
# Sort the array of coins in decreasing order.
# Initialize ans vector as empty.
# Find the largest denomination that is smaller than remaining amount and while it is smaller than the remaining amount:
# Add found denomination to ans. Subtract value of found denomination from amount.
# If amount becomes 0, then print ans.

def findMinCoins (inputAmount):
    denomintations = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
    lengthOfDenominations = len (denomintations)
    result = list ()
    i = lengthOfDenominations - 1
    while i >= 0:
        while denomintations[i] <= inputAmount:
            inputAmount -= denomintations[i]
            result.append (denomintations[i])
        i -= 1

    return result

if __name__ == '__main__':
    print (findMinCoins (93))

# Time Complexity: O(V).
# Auxiliary Space: O(V).