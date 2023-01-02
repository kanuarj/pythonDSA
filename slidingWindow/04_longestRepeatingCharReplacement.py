# Check if the characters along with window can be maintained after the count of highest character from set
# is subtracted from the length of window and output is less than the specified k value 
# If not increment the left pointer and check again, this will also make changes in the hashset that holds the count of 26 characters

def characterReplacement (s : str, k : int) -> int:
    count, result, first = {}, 0, 0
    for second in range (len (s)):
        count[s[second]] = 1 + count.get (s[second], 0)
        
        while (second-first+1) - count[s[second]] > k:
            count[s[first]] -= 1
            first += 1

        result = max (result, second-first+1)
    return result

if __name__ == '__main__':
    s = "AABABBA"
    k = 1
    print (characterReplacement (s, k))
    # Input: s = "AABABBA", k = 1
    # Output: 4
    # Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
    # The substring "BBBB" has the longest repeating letters, which is 4.