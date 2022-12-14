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
# ================================================================
# Different Approach :
# The logic is very simple.
# Any integer number other than power of 3 which divides highest power of 3 value that integer can hold 3^19 = 1162261467
# (Assuming that integers are stored using 32 bits) will give reminder non-zero. 

def differentApproach (n):
    return (3**19) % n is 0

# Time Complexity : O(1)
# Auxiliary Space: O(1)


if __name__ == '__main__':
    # print (generalSolution (16))
    # print (recursiveSolution (9))
    print (differentApproach (82))