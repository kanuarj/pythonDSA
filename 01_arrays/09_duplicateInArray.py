# Find the Duplicate Number

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.

# Example 1:
# Input: nums = [1,3,4,2,2]
# Output: 2

# Example 2:
# Input: nums = [3,1,3,4,2]
# Output: 3

def duplicateFinder(input_array):
    holder = dict()

    if len(input_array) == 1:
        return input_array[0]

    for i in input_array:
        if i in holder:
            holder[i] += 1
        else:
            holder[i] = 1

    return max(holder, key=holder.get)
    
if __name__ == '__main__':
    input_array = [1,3,4,2,2]
    output = duplicateFinder(input_array)
    print(output)