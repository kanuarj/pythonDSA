# Index Mapping (or Trivial Hashing) with negatives allowed

# Given a limited range array contains both positive and non-positive numbers, i.e., elements are in the range from -MAX to +MAX.
# Task is to search if some number is present in the array or not in O(1) time.
# Since range is limited, we can use index mapping (or trivial hashing).
# Use values as the index in a big array. Therefore we can search and insert elements in O(1) time.

# How to handle negative numbers? 
# The idea is to use a 2D array of size hash[MAX+1][2]

# Algorithm:
# Assign all the values of the hash matrix as 0.
# Traverse the given array:
#     If the element ele is non negative assign 
#         hash[ele][0] as 1.
#     Else take the absolute value of ele and 
#         assign hash[ele][1] as 1.

# To search any element x in the array. 
#     If X is non-negative check if hash[X][0] is 1 or not. If hash[X][0] is one then the number is present else not present.
#     If X is negative take absolute value of X and then check if hash[X][1] is 1 or not. If hash[X][1] is one then the number is present

def search (hashMap, X):
    if X >= 0:
        return hashMap[X][0] == 1

    X = abs (X)
    return hashMap[X][1] == 1

def insert (hashMap, inputValues, lengthOfInput):
    for i in range (0, lengthOfInput):
        if inputValues[i] >= 0:
            hashMap[inputValues[i]][0] = 1
        else:
            hashMap[abs (inputValues[i])][1] = 1

if __name__ == '__main__':
    inputArray = [-1, 9, -5, -8, -5, -2]
    length = len (inputArray)
    MAX = 10
    hashmap = [[0 for i in range (2)] for j in range (MAX+1)]
    insert (hashmap, inputArray, length)
    X = -6
    if search (hashmap, X) == True:
        print ('Element Present')
    else:
        print ('Element not present')