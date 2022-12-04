def heapify (arr, N, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    # Check if the left child is greater than root
    if left < N and arr[largest] < arr[left]:
        largest = left

    # Check if the right child is greater than root
    if right < N and arr[largest] < arr[right]:
        largest = right

    # Changes in root if required
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify (arr, N, largest)

def heapSort (arr):
    N = len (arr)

    # Creation of a max heap 
    for i in range (N//2 - 1, -1, -1):
        heapify (arr, N, i)

    # Extraction of elements one by one
    for i in range (N-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify (arr, i, 0)

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    heapSort (arr)
    print (f'Sorted Array using Heap Sort is {arr}')

    