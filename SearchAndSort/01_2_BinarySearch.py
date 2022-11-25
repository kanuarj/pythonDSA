# Examples: 
# Input: arr[] = {10, 20, 30, 50, 60, 80, 110, 130, 140, 170}, x = 110
# Output: 6
# Explanation: Element x is present at index 6. 

# Input: arr[] = {10, 20, 30, 40, 60, 110, 120, 130, 170}, x = 175
# Output: -1
# Explanation: Element x is not present in arr[].

# Binary Search Algorithm :
# - Compare x with the middle element.
# - If x matches with the middle element, we return the mid index.
# - Else If x is greater than the mid element, then x can only lie in the right half subarray after the mid element. 
#       So we recur for the right half.
# - Else (x is smaller) recur for the left half.

class RecursiveBinarySearch:
    def binarySearch (self, arr, start, end, key):
        if end >= start:
            middle = start + (end - start) // 2
            if arr[middle] == key:
                return middle
            elif arr[middle] > key:
                return self.binarySearch (arr, start, middle-1, key)
            else:
                return self.binarySearch (arr, middle+1, end, key)
        else:
            return -1

# Time Complexity: O(log n)
# Auxiliary Space: O(log n)

class IterativeBinarySearch:
    def __init__(self, arr, key):
        self.start = 0
        self.arr = arr
        self.end = len(arr)
        self.key = key

    def binarySearch (self):
        while self.start <= self.end:
            middle = self.start + (self.end - self.start) // 2
            if arr[middle] == key:
                return middle
            elif arr[middle] < key:
                self.start = middle + 1
            else:
                self.end = middle - 1
        return -1

# Time Complexity: O(log n)
# Auxiliary Space: O(1)

if __name__ == '__main__':
    arr = [1, 2, 5, 7, 9]
    key = 3
    bSearch = IterativeBinarySearch (arr, key)
    outcome = bSearch.binarySearch ()
    print (f'The index of searched index is {outcome}')

