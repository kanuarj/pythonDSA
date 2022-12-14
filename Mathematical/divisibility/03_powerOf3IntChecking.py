# Find whether a given integer is a power of 3 or not

# Examples: 
# Input : 3
# Output :Yes

# Input :6
# Output :No

import math

# General Solution
def generalSolution (n):
    logValue = math.log (n) / math.log (3)
    return (logValue - int (logValue)) == 0

# Time Complexity: O(1)
# Space Complexity: O(1)
# ========================================================
# Recursive Solution 
def recursiveSolution (n):
    if n <= 0:
        return False

    if n is 1:
        return True

    if n % 3 is 0:
        return recursiveSolution (n // 3)

    return False

# Time Complexity: O(log3n), where n represents the given integer.
# Auxiliary Space: O(log3n).

if __name__ == '__main__':
    # print (generalSolution (16))
    print (recursiveSolution (9))