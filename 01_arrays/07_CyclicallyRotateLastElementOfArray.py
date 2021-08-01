def cyclically_rotate (array):
    n = len(array)
    x = array[n-1]
    for i in range(n-1, 0, -1):
        array[i] = array[i - 1]    
    array[0] = x
    return array


if __name__ == '__main__':
    array = [1,2,3,4,5,6]
    output = cyclically_rotate(array)
    print(output)