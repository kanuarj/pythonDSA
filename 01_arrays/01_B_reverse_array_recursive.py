class RecursiveReverseArray:
    
    def __init__(self, input_array):
        self.input_array = input_array
        self.start = 0
        self.end = len(input_array) - 1

    def recursion(self):
        if self.start >= self.end:
            return self.input_array
        
        self.input_array[self.start], self.input_array[self.end] = self.input_array[self.end], self.input_array[self.start]
        self.start += 1
        self.end -= 1
        return self.recursion()

if __name__ == '__main__':
    array_as_input = [1,2,3,4,5,6,7,8,9]
    print(f'Input Array : {array_as_input}')
    rra_object = RecursiveReverseArray(array_as_input)
    output_array = rra_object.recursion()
    print(f'Output Array : {output_array}')