# Check if a large number is divisible by 3 or not

# Examples: 
# Input  : n = 769452
# Output : Yes

# Input  : n = 123456758933312
# Output : No

# Input  : n = 3635883959606670431112222
# Output : Yes

def checkIsDivisible (n):
    digitSum = 0
    while n > 0:
        rem = n % 10
        digitSum += rem
        n //= 10
    
    return (digitSum % 3 == 0)

# Time Complexity: O(logn), where n is the given number.
# Auxiliary Space: O(1), as we are not using any extra space. 

if __name__ == '__main__':
    print (checkIsDivisible (3635883959606670431112222))