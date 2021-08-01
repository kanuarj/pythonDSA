def reverseArray(input_array):
    start = 0
    end = len(input_array) - 1
    
    while start < end:
        input_array[start], input_array[end] = input_array[end], input_array[start]
        start += 1
        end -= 1
    return input_array

if __name__ == '__main__':
    array = [9,8,7,6,5,4,3,2,1]
    reversed_array = reverseArray(array)
    print(reversed_array)