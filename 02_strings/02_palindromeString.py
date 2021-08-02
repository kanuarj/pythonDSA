def palindrome(input_string):
    reverse_string = input_string[::-1]
    if reverse_string == input_string:
        return f'{input_string} is a Palindrome String'
    else:
        return f'{input_string} is not a Palindrome String'

if __name__ == '__main__':
    input_string = 'abca'
    output = palindrome(input_string)
    print(output)