# Given an array of integers arr[] of size N and an integer, the task is to rotate the array elements to the left by d positions.

# Examples:
# Input: arr[] = {1, 2, 3, 4, 5, 6, 7}, d = 2
# Output: 3 4 5 6 7 1 2

# Input: arr[] = {3, 4, 5, 6, 7, 1, 2}, d=2
# Output: 5 6 7 1 2 3 4


# Using Temp Array Approach that has O(N) time complexity as well as space complexity.

# Implementation Steps :
# - Initialize (temp[n]) of length same as the original array
# - Initialize an integer(k) to keep a track of the current index
# - Store the elements from the position d to n-1 in the temporary array
# - Now, store 0 to d-1 elements of the original array in the temporary array
# - Lastly, copy back the temporary array to the original array

class arrayRotation:
    tempArray = list()

    def rotateArray (self, inputArray, rotationElement):
        indexElement = inputArray.index(rotationElement)
        self.tempArray = inputArray[indexElement+1:] + inputArray[0:indexElement+1]
        return self.tempArray


if __name__ == '__main__':
    ar = arrayRotation()
    arr = [1, 2, 3, 4, 5, 6, 7]
    d = 2
    arr = ar.rotateArray (arr, d)
    print ("Final Output", arr)
