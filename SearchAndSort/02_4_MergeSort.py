# Time Complexity: O(N log(N))
# Auxiliary Space: O(n)

# Algorithm:
# step 1: start

# step 2: declare array and left, right, mid variable

# step 3: perform merge function.
#     if left > right
#         return
#     mid= (left+right)/2
#     mergesort(array, left, mid)
#     mergesort(array, mid+1, right)
#     merge(array, left, mid, right)

# step 4: Stop

class MergeSort:
    def sortingFunction (self, arr):
        if len(arr) > 1:

            # Find the middle of the array for creating division
            mid = len(arr) // 2

            # Splitting the array in 2 portions of left and right 
            left = arr[:mid]
            right = arr[mid:]

            # Sorting the 2 different portions of array separately 
            self.sortingFunction (left)
            self.sortingFunction (right)

            # Copy the sorted data to respective 2 portions of array 
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            # Checking the left over elements and adding them to final array
            while i < len(left):
                arr[k] = left[i]
                i+=1
                k+=1

            while j < len(right):
                arr[k] = right[j]
                j+=1
                k+=1

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    sort = MergeSort ()
    sort.sortingFunction (arr)
    print (f'Sorted array is given as {arr}')



