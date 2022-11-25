# Follow the below steps to solve the problem:
# - Initialize minimum value(min_idx) to location 0.
# - Traverse the array to find the minimum element in the array.
# - While traversing if any element smaller than min_idx is found then swap both the values.
# - Then, increment min_idx to point to the next element.
# - Repeat until the array is sorted.

# Time Complexity: 
# The time complexity of Selection Sort is O(N2) as there are two nested loops:
# One loop to select an element of Array one by one = O(N)
# Another loop to compare that element with every other Array element = O(N)
# Therefore overall complexity = O(N) * O(N) = O(N*N) = O(N2)

# Auxiliary Space: O(1) as the only extra memory used is for temporary variables while swapping two values in Array.
#                 The selection sort never makes more than O(N) swaps and can be useful when memory write is a costly operation. 

class SelectionSort:
    def sortFunction (self, arr):
        for i in range (len(arr)):
            minElementIndex = i
            for j in range (i+1, len(arr)):
                if (arr[minElementIndex] > arr[j]):
                    minElementIndex = j
            arr[minElementIndex], arr[i] = arr[i], arr[minElementIndex]


if __name__ == '__main__':
    arr = [64, 25, 12, 22, 11]
    sort = SelectionSort ()
    sort.sortFunction (arr)
    print (arr)