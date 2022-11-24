# Given an array (or string), the task is to reverse the array/string.

# Examples : 
# Input  : arr[] = {1, 2, 3}
# Output : arr[] = {3, 2, 1}

# Input :  arr[] = {4, 5, 1, 2}
# Output : arr[] = {2, 1, 5, 4}

# Iterative way : Time Complexity : O(n)
# 1) Initialize start and end indexes as start = 0, end = n-1 
# 2) In a loop, swap arr[start] with arr[end] and change start and end as follows : 
#   start = start +1, end = end – 1

class IterativeReverseApproach:
    def reverseArrayElements (self, inputArray):
        start, end = 0, len(inputArray) - 1
        while start < end:
            inputArray[start], inputArray[end] = inputArray[end], inputArray[start]
            start += 1
            end -= 1

# Recursive Way : Time Complexity : O(n)
# 1) Initialize start and end indexes as start = 0, end = n-1 
# 2) Swap arr[start] with arr[end] 
# 3) Recursively call reverse for rest of the array.

class RecursiveReverseApproach:
    def reverseArrayElements (self, inputArray, start, end):
        if start >= end:
            return
        inputArray[start], inputArray[end] = inputArray[end], inputArray[start]
        self.reverseArrayElements (inputArray, start+1, end-1)

# Using Python List Slicing
class ListSlicing:
    def reverseList (self, inputArray):
        return inputArray[::-1]

if __name__ == '__main__':
    arr = [2, 1, 5, 4]
    iterative = ListSlicing ()
    arr = iterative.reverseList (arr)
    print (arr)