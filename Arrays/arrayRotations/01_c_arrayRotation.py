def rotateArray (inputArray, rotationElement, lengthOfArray):
    rotationElement %= lengthOfArray
    gcd = gcdFunction (rotationElement, lengthOfArray)

    for i in range(gcd):
        temp = inputArray[i]
        j = i
        while True:
            k = j + rotationElement
            if k >= lengthOfArray:
                k -= lengthOfArray
            if k == i:
                break

            inputArray[j] = inputArray[k]
            j = k
        inputArray[j] = temp



def gcdFunction (firstNumber, secondNumber):
    if (secondNumber == 0):
        return firstNumber
    else:
        return gcdFunction (secondNumber, firstNumber % secondNumber)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    d = 2
    rotateArray (arr, d, len(arr))
    print (f"Final Output is {arr}")