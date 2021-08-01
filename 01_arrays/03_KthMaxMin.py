'''
Given an array array and a number K where K is smaller than size of array,
the task is to find the Kth min element and max element in the given array.
It is given that all array elements are distinct.

Example:
Input:
arr = [10,32,22,45,6]
K = 4
Output : 32 Min, 10 Max
Explanation :
4th min element in the given array is 32 since [6,10,22,32,45].
'''

def kth_max_min(input_array, k):
    if k < len(input_array):
        sorted_array = sorted(input_array)
        reversed_array = sorted(input_array, reverse=True)
        minimum_value = sorted_array[k-1]
        maximum_value = reversed_array[k-1]
    return minimum_value, maximum_value

if __name__ == '__main__':
    arr = [10,32,22,45,6]
    k = 4
    minimum, maximum = kth_max_min(arr, k)
    print(f'Min Number on {k} position is {minimum}\nMax Number on {k} position is {maximum}')