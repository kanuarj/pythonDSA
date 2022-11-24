# Follow the given steps to solve the problem:
# - Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
# - If x matches with an element, return the index.
# - If x doesn’t match with any of the elements, return -1.
# Time complexity: O(N)
# Auxiliary Space: O(1)

class LinearSearchIterative:
    def linearSearch (self, arr, x):
        for i in range(len(arr)):
            if arr[i] == x:
                return i
        return -1

# Linear Search Recursive Approach:
# Follow the given steps to solve the problem:
# If the size of the array is zero then, return -1, representing that the element is not found. This can also be treated as the base condition of a recursion call.
# Otherwise, check if the element at the current index in the array is equal to the key or not i.e, arr[size – 1] == key
# If equal, then return the index of the found key.
# Time Complexity: O(N)
# Auxiliary Space: O(N), for using recursive stack space. 

class LinearSearchRecursive:
    def linearSearch (self, arr, key, size):
        if (size == 0):
            return -1
        elif (arr[size-1] == key):
            return size-1
        else:
            return self.linearSearch (arr, key, size-1)

if __name__ == '__main__':
    arr = [5, 15, 6, 9, 4]
    key = 6
    search = LinearSearchRecursive ()
    outcome = search.linearSearch (arr, key, len(arr))
    print (outcome)




