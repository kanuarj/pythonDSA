# Given an array of n elements. Our task is to write a program to rearrange the array such that
# elements at even positions are greater than all elements before it
# and elements at odd positions are less than all elements before it.

# Examples: 
# Input : arr[] = {1, 2, 3, 4, 5, 6, 7}
# Output : 4 5 3 6 2 7 1

# Input : arr[] = {1, 2, 1, 4, 5, 6, 8, 8} 
# Output : 4 5 2 6 1 8 1 8

# The idea to solve this problem is to first create an additional copy of the original array and sort the copied array.
# Now the total number of even positions in an array with n elements will be floor(n/2) and the remaining is the number of odd positions.
# Now fill the odd and even positions in the original array using the sorted array in a below manner: 
#   Total odd positions will be n – floor(n/2). Start from (n-floor(n/2))th position in the sorted array and copy the element to the 1st position of the sorted array.
#       Start traversing the sorted array from this position towards the left and keep filling the odd positions in the original array towards the right.
#   Start traversing the sorted array starting from (n-floor(n/2)+1)th position towards the right and keep filling the original array starting from the 2nd position. 

# Time Complexity: O( n logn ) 
# Auxiliary Space: O(n)

def rearrangeFunction (arr, n):
    # Total number of even positions 
    evenPositions = n // 2
    # Total number of odd positions 
    oddPositions = n - evenPositions
    # Creation of a temporary array
    tempArr = []

    # Copy all the elements of original array to temp array
    for i in arr:
        tempArr.append (i)

    # Sort all the elements in temporary array
    tempArr.sort ()

    # Filling up the odd positions in array
    j = oddPositions - 1
    for i in range (0, n, 2):
        arr[i] = tempArr[j]
        j -= 1

    # Filling up the even positions in array
    j = oddPositions
    for i in range (1, n, 2):
        arr[i] = tempArr[j]
        j += 1

# Another Approach : We can traverse the array by defining two variables j and k and assign values from last.
# if even index is there, we will give it max value otherwise min value.
# j =0 and k= end. j will go ahead and k will decrease.

# Time Complexity: O(n log n), The maximum time taken to sort the array.
# Auxiliary Space: O(n), The extra space is required to store the copy of elements of original array.
def anotherRearrangingFunction (arr, n):
    # Creation of a temporary array
    temp = list ()
    # Copying all the elements from original to temp array
    for i in arr:
        temp.append (i)
    # Sorting the elements from temp array
    temp.sort ()
    # Initalization of 2 pointers for functioning
    j, k = 0, n-1
    # Loop for putting the elements in place
    for i in reversed(range (n)):
        if (i % 2 != 0):
            arr[i] = temp[k]
            k -= 1
        else:
            arr[i] = temp[j]
            j += 1

if __name__ == '__main__':
    arr = [1, 2, 1, 4, 5, 6, 8, 8]
    anotherRearrangingFunction (arr, len(arr))
    print (arr)