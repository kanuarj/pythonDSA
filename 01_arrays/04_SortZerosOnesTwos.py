'''
Sort an array of 0s, 1s and 2s : 
Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.

Tip : Solve using DUTCH NATIONAL FLAG ALGORITHM
'''

def sorting_function(array):
    start, mid = 0, 0
    end = len(array) - 1

    while mid <= end:
        if array[mid] == 0:
            array[start], array[mid] = array[mid], array[start]
            start += 1
            mid += 1
        elif array[mid] == 1:
            mid += 1
        else:
            array[mid], array[end] = array[end], array[mid]
            end -= 1
    return array

if __name__ == '__main__':
    array = [1,0,0,2,1,2,0]
    output = sorting_function(array)
    print('Sorted Array :',output)