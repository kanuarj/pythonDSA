class ReverseString:

    def __init__(self, array):
        self.array = array
        self.start = 0
        self.end = len(array) - 1

    def reverse(self):
        while self.start <= self.end:
            self.array[self.start], self.array[self.end] = self.array[self.end], self.array[self.start]
            self.start += 1
            self.end -= 1
        return self.array

if __name__ == '__main__':
    inputArray = ['s','t','r','i','n','g']
    reverseStringObject = ReverseString(inputArray)
    output = reverseStringObject.reverse()  
    print(output)