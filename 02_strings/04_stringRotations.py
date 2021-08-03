# A Program to check if strings are rotations of each other or not
# Given a string s1 and a string s2, write a snippet to say whether s2 is a rotation of s1? 
# (eg given s1 = ABCD and s2 = CDAB, return true, given s1 = ABCD, and s2 = ACBD , return false)

# Algorithm :
# 1. Create a temp string and store concatenation of str1 to str1 in temp.
#                           temp = str1.str1
# 2. If str2 is a substring of temp then str1 and str2 are rotations of each other.

# Example:                 
#                      str1 = "ABACD"
#                      str2 = "CDABA"

#      temp = str1.str1 = "ABACDABACD"
#      Since str2 is a substring of temp, str1 and str2 are 
#      rotations of each other.

def stringRotations(string_1, string_2):
    temp = string_1 + string_1
    if string_2 in temp:
        return True
    else:
        return False

if __name__ == '__main__':
    string_1 = 'ABACD'
    string_2 = 'CDABA'
    output = stringRotations(string_1, string_2)
    print(output)