# Time Complexity: O(N^2) 
# Auxiliary Space: O(1)

# Insertion Sort Algorithm to sort an array of size N in ascending order: 
# - Iterate from arr[1] to arr[N] over the array. 
# - Compare the current element (key) to its predecessor. 
# - If the key element is smaller than its predecessor, compare it to the elements before.
#     Move the greater elements one position up to make space for the swapped element.

class InsertionSort:
    def sortingFunction (self, arr):
        for i in range (1, len(arr)):
            j = i-1
            x = arr[i]
            while (j>=0 and x < arr[j]):
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = x

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6]
    sort = InsertionSort ()
    sort.sortingFunction (arr)
    print (arr)