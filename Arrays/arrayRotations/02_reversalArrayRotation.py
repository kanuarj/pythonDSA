# Reversal Algorithm for Array Rotations from a given point 

# Examples: 
# Input:  arr[] = {1, 2, 3, 4, 5, 6, 7}, d = 2
# Output: 3, 4, 5, 6, 7, 1, 2
# Explanation: If the array is rotated by 1 position to the left, 
# it becomes {2, 3, 4, 5, 6, 7, 1}.
# When it is rotated further by 1 position,
# it becomes: {3, 4, 5, 6, 7, 1, 2}

# Input: arr[] = {1, 6, 7, 8}, d = 3
# Output: 8, 1, 6, 7

class ReversalAlgorithm:
    def rotateArray (self, arr, start, end):
        while (start < end):
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
            start += 1
            end -= 1

    def leftReversal (self, arr, key):
        if key == 0:
            return
        n = len (arr)
        key %= n
        self.rotateArray (arr, 0, key-1)
        self.rotateArray (arr, key, n-1)
        self.rotateArray (arr, 0, n-1)

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    reversal = ReversalAlgorithm ()
    reversal.leftReversal (arr, 2)
    print(f'The array after rotation based on given key is {arr}')

