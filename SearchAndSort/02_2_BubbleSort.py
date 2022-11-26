# Time Complexity: O(N2)
# Auxiliary Space: O(1) 

class BubbleSort:
    def iterativeSort (self, arr):
        n = len (arr)
        for i in range (n):
            for j in range (0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

    def recursiveSort (self, arr, arrLen):
        if (arrLen == 0 or arrLen == 1):
            return
        for i in range (arrLen-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        self.recursiveSort (arr, arrLen-1)

if __name__ == '__main__':
    arr = [5, 1, 4, 2, 8]
    sort = BubbleSort ()
    sort.recursiveSort (arr, len(arr))
    print (arr)