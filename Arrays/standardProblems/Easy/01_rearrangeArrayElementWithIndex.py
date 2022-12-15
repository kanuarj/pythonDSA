# Rearrange an array such that arr[i] = i

# Given an array of elements of length N, ranging from 0 to N – 1.
# All elements may not be present in the array. If the element is not present then there will be -1 present in the array.
# Rearrange the array such that A[i] = i and if i is not present, display -1 at that place.

# Examples: 
# Input : arr = {-1, -1, 6, 1, 9, 3, 2, -1, 4, -1}
# Output : [-1, 1, 2, 3, 4, -1, 6, -1, -1, 9]

# Input : arr = {19, 7, 0, 3, 18, 15, 12, 6, 1, 8,
#               11, 10, 9, 5, 13, 16, 2, 14, 17, 4}
# Output : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
#          11, 12, 13, 14, 15, 16, 17, 18, 19]

# Naive Approach :
#     Nav­i­gate the numbers from 0 to n-1.
#     Now navigate through array.
#     If (i==a[j]) , then replace the element at i position with a[j] position.
#     If there is any element in which -1 is used instead of the number then it will be replaced automatically.
#     Now, iterate through the array and check if (a[i]!=i) , if it s true then replace a[i] with -1.

def naiveApproach (arr, n):
    for i in range (n):
        for j in range (n):
            if arr[j] == i:
                arr[j], arr[i] = arr[i], arr[j]

    for k in range (n):
        if arr[k] is not k:
            arr[k] = -1

# Time Complexity: O(n^2)
# Auxiliary Space: O(1), since no extra space has been taken.

# ===================================================================================================
# Another Approach: 
# 1. Nav­i­gate through the array. 
# 2. Check if a[i] = -1, if yes then ignore it. 
# 3. If a[i] != -1, Check if element a[i] is at its cor­rect posi­tion (i=A[i]). If yes then ignore it. 
# 4. If a[i] != -1 and ele­ment a[i] is not at its cor­rect posi­tion (i!=A[i]) then place it to its correct posi­tion, but there are two conditions:  

#     Either A[i] is vacate, means A[i] = -1, then just put A[i] = i.
#     OR A[i] is not vacate, means A[i] = x, then int y=x put A[i] = i. Now, we need to place y to its cor­rect place, so repeat from step 3.

def anotherApproach (arr, n):
    for i in range (0, n):
        if arr[i] is not -1 and arr[i] is not i:
            x = arr[i]

            while (arr[x] is not -1 and arr[x] is not x):
                y = arr[x]
                arr[x] = x
                x = y

            arr[x] = x

            if arr[i] is not i:
                arr[i] = -1

# Time Complexity: O(n)
# Auxiliary Space: O(1)

# ================================================================================================
# Approach using Set 
# 1) Store all the numbers present in the array into a Set 
# 2) Iterate through the length of the array, if the corresponding position element is present in the Set, then set A[i] = i, else A[i] = -1

def usingSet (arr, n):
    s = set ()
    for i in range (n):
        s.add (arr[i])

    for i in range (n):
        if i in s:
            arr[i] = i
        else:
            arr[i] = -1

# Time Complexity: O(n)
# Auxiliary Space: O(n)

# ==================================================================================================
# Approach using Cyclic Sort 
# 1) Iterate through elements in an array 
# 2) If arr[i] >= 0 && arr[i] != i, put arr[i] at i ( swap arr[i] with arr[arr[i]])

def usingCycleSort (arr, n, i=0):
    while i < n:
        if arr[i] >= 0 and arr[i] is not i:
            arr[arr[i]], arr[i] = arr[i], arr[arr[i]]
        else:
            i += 1

# Time Complexity: O(n)
# Auxiliary Space: O(1)

if __name__ == '__main__':
    arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
    # naiveApproach (arr, len(arr))
    # anotherApproach (arr, len(arr))
    # usingSet (arr, len(arr))
    usingCycleSort (arr, len (arr))
    print (f'The final output array is given by {arr}')