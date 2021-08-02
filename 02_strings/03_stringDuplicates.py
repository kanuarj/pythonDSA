from collections import defaultdict

def duplicates(input_string):
    count = defaultdict(int)
    for i in range(len(input_string)):
        count[input_string[i]] += 1

    for x in count:
        if count[x] > 1:
            print (f'{x} with counts {count[x]}')

if __name__ == '__main__':
    input_string = input('Please enter the string.\n')
    duplicates(input_string)