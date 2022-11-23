# Given an array of integers arr[] of size N and an integer, the task is to rotate the array elements to the left by d positions.

# Examples:
# Input: arr[] = {1, 2, 3, 4, 5, 6, 7}, d = 2
# Output: 3 4 5 6 7 1 2

# Input: arr[] = {3, 4, 5, 6, 7, 1, 2}, d=2
# Output: 5 6 7 1 2 3 4

# Array Rotation using the Juggling Method that uses O(N) time complexity and O(1) space complexity.

# Steps for implementation :
# - Perform d%n in order to keep the value of d within the range of the array where d is the number of times the array is rotated
#   and N is the size of the array.
# - Calculate the GCD(N, d) to divide the array into sets.
# - Run a for loop from 0 to the value obtained from GCD.
#     - Store the value of arr[i] in a temporary variable (the value of i denotes the set number).
#     - Run a while loop to update the values according to the set.
# - After exiting the while loop assign the value of arr[j] as the value of the temporary
#   variable (the value of j denotes the last element of the ith set).

class arrayRotationUsingJugglingMethod:
    def rotateArray (self, inputArray, rotationElement, lengthOfArray):
        rotationElement %= lengthOfArray
        gcd = self.gcdFunction (rotationElement, lengthOfArray)

        for i in range(gcd):
            temp = inputArray[i]
            j = i
            while True:
                k = j + rotationElement
                if k >= lengthOfArray:
                    k -= lengthOfArray
                if k == i:
                    break

                inputArray[j] = inputArray[k]
                j = k
            inputArray[j] = temp


    def gcdFunction (self, firstNumber, secondNumber):
        if (secondNumber == 0):
            return firstNumber
        else:
            return self.gcdFunction (secondNumber, firstNumber % secondNumber)


if __name__ == '__main__':
    ar = arrayRotationUsingJugglingMethod()
    arr = [1, 2, 3, 4, 5, 6, 7]
    d = 2
    ar.rotateArray (arr, d, len(arr))
    print (f"Final Output is {arr}")