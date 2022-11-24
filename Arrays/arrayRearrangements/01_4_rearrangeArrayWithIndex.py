# Given an array of elements of length N, ranging from 0 to N – 1.
# All elements may not be present in the array.
# If the element is not present then there will be -1 present in the array.
# Rearrange the array such that A[i] = i and if i is not present, display -1 at that place.

# Examples: 
# Input : arr = {-1, -1, 6, 1, 9, 3, 2, -1, 4, -1}
# Output : [-1, 1, 2, 3, 4, -1, 6, -1, -1, 9]

# Input : arr = {19, 7, 0, 3, 18, 15, 12, 6, 1, 8, 11, 10, 9, 5, 13, 16, 2, 14, 17, 4}
# Output : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# This approach runs the time complexity in O(N) and O(1) space complexity.

# Cyclic Sort Approach (Swapping Elements in Array) :
# 1. Iterate through elements in an array 
# 2. If arr[i] >= 0 && arr[i] != i, put arr[i] at i ( swap arr[i] with arr[arr[i]])

class CyclicSortApproach:
    i = 0
    def rearrangingWithSwapping (self, inputArray):
        while self.i < len(inputArray):
            if (inputArray[self.i] >= 0 and inputArray[self.i] != self.i):
                inputArray[inputArray[self.i]], inputArray[self.i] = inputArray[self.i], inputArray[inputArray[self.i]]
            else:
                self.i += 1

if __name__ == '__main__':
    arr = [19, 7, 0, 3, 18, 15, 12, 6, 1, 8, 11, 10, 9, 5, 13, 16, 2, 14, 17, 4]
    csa = CyclicSortApproach ()
    csa.rearrangingWithSwapping (arr)
    print (f'Final Output is {arr}')