def partitionFunction (arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range (low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quickSortFunction (arr, low, high):
    if low < high:
        pivot = partitionFunction (arr, low, high)
        quickSortFunction (arr, low, pivot-1)
        quickSortFunction (arr, pivot+1, high)

if __name__ == '__main__':
    arr = [10, 7, 8, 9, 1, 5]
    quickSortFunction (arr, 0, len (arr)-1)
    print (f'Sorted Array using Quick Sort is {arr}')