# Given an array of integers arr[] of size N and an integer, the task is to rotate the array elements to the left by d positions.

# Examples:
# Input: arr[] = {1, 2, 3, 4, 5, 6, 7}, d = 2
# Output: 3 4 5 6 7 1 2

# Input: arr[] = {3, 4, 5, 6, 7, 1, 2}, d=2
# Output: 5 6 7 1 2 3 4

# Rotate One By One Approach is used which uses O(N*d) time complexity and O(1) space complexity.

# Steps for given approach :
# - Rotate the array to left by one position. For that do the following:
#     - Store the first element of the array in a temporary variable.
#     - Shift the rest of the elements in the original array by one place.
#     - Update the last index of the array with the temporary variable.
# - Repeat the above steps for the number of left rotations required.

class arrayRotationOneByOneMethod:
    holder = 1

    def arrayRotation (self, inputArray, rotationElement, lengthOfArray):
        while (self.holder <= rotationElement):
            firstElement = inputArray[0]
            for i in range (lengthOfArray - 1):
                inputArray[i] = inputArray[i+1]
            inputArray[lengthOfArray-1] = firstElement
            self.holder += 1

        return inputArray

if __name__ == '__main__':
    ar = arrayRotationOneByOneMethod ()
    arr = [1, 2, 3, 4, 5, 6, 7]
    d = 2
    arr = ar.arrayRotation (arr, d, len(arr))
    print (f"Final Output is {arr}")