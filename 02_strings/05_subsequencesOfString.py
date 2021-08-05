def subsequence(string_input, output_string):
    if len(string_input) == 0:
        print(output_string, end=' ')
        return

    subsequence(string_input[1:], output_string + string_input[0])
    subsequence(string_input[1:], output_string)

if __name__ == '__main__':
    input_string = 'abc'
    output_string = ''
    subsequence(input_string, output_string)