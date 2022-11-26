# // Whenever asked to sort the element 1-N, always use Cycle Sort.
# // The algorithm has worst case time complexity as O(N).
# // The algorithm also performs sorting in-place and there is no substantial requirement of extra space.
# // The algorithm always will place the correct index with the number of element minus one.
# // The algorithm is commonly used for FAANG based interviews.

# Time Complexity Analysis:
# Worst Case : O(n) 
# Average Case: O(n) 
# Best Case : O(n)

# Auxiliary Space: O(1)

class CyclicSort:
    def sortingFunction (self, arr, n):
        i = 0
        while i < n:
            correctPosition = arr[i] - 1
            if (arr[i] < n and arr[i] is not arr[correctPosition]):
                temp = arr[i]
                arr[i] = arr[correctPosition]
                arr[correctPosition] = temp
            else:
                i += 1

if __name__ == '__main__':
    arr = [3, 2, 4, 5, 1]
    sort = CyclicSort ()
    sort.sortingFunction (arr, len(arr))
    print (arr)