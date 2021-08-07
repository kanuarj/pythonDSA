# Examples:

# Input: str = "abc"
# Output: 0
# There is no repeating subsequence

# Input: str = "aab"
# Output: 1
# The two subssequence are 'a'(first) and 'a'(second). Note that 'b' cannot be considered as part of subsequence 
# as it would be at same index in both.

# Input: str = "aabb"
# Output: 2

# Input: str = "axxxy"
# Output: 2

def LCS(input_string):
    string_length = len(input_string)

    matrix = [[0 for i in range(string_length + 1)] for j in range(string_length + 1)]

    for i in range(1, string_length + 1):
        for j in range(1, string_length + 1):
            if input_string[i-1] == input_string[j-1] and i !=j:
                matrix[i][j] = 1 + matrix[i-1][j-1]
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

    return matrix[string_length][string_length]
            
if __name__ == '__main__':
    string = 'aabbcc'
    value = LCS(string)
    print(value)