'''
Move all negative numbers to beginning and positive to end. Order is not important.

Two Pointer Approach :
1. Check If the left and right pointer elements are negative then simply increment the left pointer.
2. Otherwise, if the left element is positive and the right element is negative then simply swap the elements,
and simultaneously increment and decrement the left and right pointers.
3. Else if the left element is positive and the right element is also positive then simply decrement the right pointer.
4. Repeat the above 3 steps until the left pointer ≤ right pointer.
'''

def negative_numbers_mover(array):
    left_pointer = 0
    right_pointer = len(array) - 1

    while left_pointer <= right_pointer:
        if array[left_pointer] < 0 and array[right_pointer] < 0:
            left_pointer += 1
        elif array[left_pointer] > 0 and array[right_pointer] < 0:
            array[left_pointer], array[right_pointer] = array[right_pointer], array[left_pointer]
            left_pointer += 1
            right_pointer -= 1
        elif array[left_pointer] > 0 and array[right_pointer] > 0:
            right_pointer -=1
        else:
            left_pointer += 1
            right_pointer -= 1

    return array

if __name__ == '__main__':
    array = [-10, 3, -7, 32, 66, -55, 88, -95]
    output = negative_numbers_mover(array)
    print(output)
