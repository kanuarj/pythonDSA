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

if __name__ == '__main__':
    print (generalSolution (16))