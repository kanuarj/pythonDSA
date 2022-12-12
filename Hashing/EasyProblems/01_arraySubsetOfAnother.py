# Find whether an array is a subset of another array using Hashing :
# The idea is to insert all the elements of the first array in a HashSet, and then iterate on the second array and
# find if the element exists in the HashSet, if the HashSet doesn’t contain any particular value then the second array
# is not the subset of the first array.

# Algorithm:
# Store the first array arr1[] in a HashSet.
# Look for the elements of arr2[] in the HashSet.
# If we encounter a particular value that is present in arr2[] but not in the HashSet, the code will terminate,
#     arr2[] can never be the subset of arr1[].
# Else arr2[] is the subset of arr1[].

def isSubsetUsingHashset (firstArr, secondArr, firstLength, secondLength):
    hashset = set ()
    for i in range (0, firstLength):
        hashset.add (firstArr[i])

    for i in range (0, secondLength):
        if secondArr[i] in hashset:
            continue
        else:
            return False

    return True

# Time Complexity: O(n*logn)
# Auxiliary Space: O(n)

if __name__ == '__main__':
    firstArr = [11, 1, 13, 21, 3, 7]
    secondArr = [9]
    firstLength = len (firstArr)
    secondLength = len (secondArr)
    print (isSubsetUsingHashset (firstArr, secondArr, firstLength, secondLength))
