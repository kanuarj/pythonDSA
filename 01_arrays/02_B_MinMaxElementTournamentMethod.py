def tournamentMethod (input_array, start, end):

    if start == end:
        minimum = input_array[start]
        maximum = input_array[start]
        return minimum, maximum
    
    elif end == start + 1:
        if input_array[start] > input_array[end]:
            minimum = input_array[end]
            maximum = input_array[start]
        else:
            minimum = input_array[start]
            maximum = input_array[end]
        return minimum, maximum

    else:
        mid_term = (start + end) // 2
        minimum_1, maximum_1 = tournamentMethod (input_array, start, mid_term)
        minimum_2, maximum_2 = tournamentMethod (input_array, mid_term + 1, end)

    return min(minimum_1, minimum_2), max(maximum_1, maximum_2)

if __name__ == '__main__':
    input_array = [1,443,66,45,87,2,2034]
    minimum_element, maximum_element = tournamentMethod(input_array, 0, len(input_array)-1)
    print('Min Element :',minimum_element)
    print('Max Element :',maximum_element)