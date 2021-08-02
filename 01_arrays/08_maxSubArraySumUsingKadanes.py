# Use the Kadane's Algorithm.
# It states that compare the number with previous and select the maximum number.
# Select the highest number spotted.

def kadanes_algorithm(array):
    maximum_compared_number = array[0]
    current_highest_value = array[0]

    for i in range(1, len(array)):
        maximum_compared_number = max(array[i], maximum_compared_number + array[i])
        current_highest_value = max(current_highest_value, maximum_compared_number)
    
    return current_highest_value

if __name__ == '__main__':
    array = [1,-4,2,-6,-9,2,1,0]
    output = kadanes_algorithm(array)
    print(output)