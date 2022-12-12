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
# ====================================================================================
# Find whether an array is a subset of another array using Set
# The idea is to insert all the elements of the first array and second array in the set,
# if the size of the set is equal to the size of arr1[] then the arr2[] is the subset of arr1[].
# As no new elements are found in arr2[] hence is the subset.

# Algorithm:
# Store the first array arr1[] in a Set.
# Store the first array arr1[] in the same Set.
# If the size of arr1[] = size of the Set, arr2[] is the subset of arr1[].
# Else arr2[] is not the subset of arr1[].

def isSubsetUsingSet (firstArr, secondArr):
    s = set ()
    firstLength = len (firstArr)
    secondLength = len (secondArr)

    for i in range (firstLength):
        s.add (firstArr[i])

    lengthOfSetAfterFirstInsertion = len (s)

    for j in range (secondLength):
        s.add (secondArr[j])

    if lengthOfSetAfterFirstInsertion == len (s):
        return True
    else:
        return False

# Time Complexity: O(m+n) because we are using unordered_set and inserting in it,
#     If we would be using an ordered set inserting would have taken log n increasing the TC to O(mlogm+nlogn),
#     but order does not matter in this approach.
# Auxiliary Space: O(n+m)


if __name__ == '__main__':
    firstArr = [11, 1, 13, 21, 3, 7]
    secondArr = [11, 21]
    firstLength = len (firstArr)
    secondLength = len (secondArr)
    # print (isSubsetUsingHashset (firstArr, secondArr, firstLength, secondLength))
    print (isSubsetUsingSet (firstArr, secondArr))
