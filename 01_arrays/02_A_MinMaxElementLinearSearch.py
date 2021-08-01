def min_max_array_element(input_array):
    min_element = 0
    max_element = 0
    array_len = len(input_array)

    if array_len == 1:
        min_element = input_array[0]
        max_element = input_array[0]
        return min_element, max_element

    if input_array[0] > input_array[1]:
        min_element = input_array[1]
        max_element = input_array[0]
    else:
        min_element = input_array[0]
        max_element = input_array[1]

    for i in range(2, array_len):
        if input_array[i] > max_element:
            max_element = input_array[i]
        elif input_array[i] < min_element:
            min_element = input_array[i]

    return min_element, max_element

if __name__ == '__main__':
    input_array = [1,34,65,88,1000,22]
    minimum_element, maximum_element = min_max_array_element(input_array)
    print('Min Number :', minimum_element)
    print('Max Number :', maximum_element)