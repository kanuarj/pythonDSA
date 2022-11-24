# Given an array of elements of length N, ranging from 0 to N – 1.
# All elements may not be present in the array.
# If the element is not present then there will be -1 present in the array.
# Rearrange the array such that A[i] = i and if i is not present, display -1 at that place.

# Examples: 
# Input : arr = {-1, -1, 6, 1, 9, 3, 2, -1, 4, -1}
# Output : [-1, 1, 2, 3, 4, -1, 6, -1, -1, 9]

# Input : arr = {19, 7, 0, 3, 18, 15, 12, 6, 1, 8, 11, 10, 9, 5, 13, 16, 2, 14, 17, 4}
# Output : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# This approach runs the time complexity in O(N) and O(N) space complexity.

# Set Storing Approach :
# 1. Store all the numbers present in the array into a Set 
# 2. Iterate through the length of the array, if the corresponding position element is present in the Set,
#     then set A[i] = i, else A[i] = -1

class SetBasedApproach:
    setHolder = set ()
    def rearrangeArrayWithIndex (self, inputArray):
        for i in inputArray:
            self.setHolder.add(inputArray[i])

        for i in range (len (inputArray)):
            if i in self.setHolder:
                inputArray[i] = i
            else:
                inputArray[i] = -1


if __name__ == '__main__':
    ar = SetBasedApproach ()
    arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
    ar.rearrangeArrayWithIndex (arr)
    print (f'Final Output is {arr}')
