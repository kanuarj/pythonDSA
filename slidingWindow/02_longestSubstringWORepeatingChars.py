# The set holds the unique characters
# If the characters are available in the set, the removal of character from left is done 
# Then the left is incremented for window. This condition is checked entirely and maximum count of such is maintained
# The value of first pointer is subtracted from second to obtain the length of the result
# This value is stored uniquely and retained with maximum value throughout

def lengthOfLongestSubstring (s : str) -> int:
    characterSet = set ()
    first = result = 0
    for second in range (len (s)):
        while s[second] in characterSet:
            characterSet.remove (s[first])
            first += 1
        characterSet.add (s[second])
        result = max (result, second-first+1)
    return result

if __name__ == '__main__':
    s = "abcabcbb"
    print (lengthOfLongestSubstring (s))
    # Input: s = "abcabcbb"
    # Output: 3
    # Explanation: The answer is "abc", with the length of 3.