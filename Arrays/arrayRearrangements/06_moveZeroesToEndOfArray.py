# Given an array of random numbers, Push all the zero’s of a given array to the end of the array.
# For example, if the given arrays is {1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0}, it should be changed to {1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0}.
# The order of all other elements should be same. Expected time complexity is O(n) and extra space is O(1).

# Example: 
# Input :  arr[] = {1, 2, 0, 4, 3, 0, 5, 0};
# Output : arr[] = {1, 2, 4, 3, 5, 0, 0, 0};

# Input : arr[]  = {1, 2, 0, 0, 0, 3, 6};
# Output : arr[] = {1, 2, 3, 6, 0, 0, 0};

def pushZeroToEndSimpleApproach (arr, lengthOfArray):
    count = 0
    for i in range (lengthOfArray):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    while count < lengthOfArray:
        arr[count] = 0
        count += 1

# Time Complexity: O(n) where n is the size of elements of the input array.
# Auxiliary Space: O(1)
# ==========================================================================================
# Method 2: Partitioning the array
# Approach:
# The approach is pretty simple. We will use 0 as a pivot element and whenever we see a non zero element we will swap it with the pivot element.
# So all the non zero element will come at the beginning.
def pushZeroToEndPartioningApproach (arr, lengthOfArray):
    j = 0
    for i in range (lengthOfArray):
        if arr[i] is not 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1

# Time Complexity: O(N), where N is the size of elements of the input array.
# Auxiliary Space: O(1) 

if __name__ == '__main__':
    arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
    n = len(arr)
    # pushZeroToEndSimpleApproach (arr, n)
    pushZeroToEndPartioningApproach (arr, n)
    print("Array after pushing all zeros to end of array:")
    print(arr)

