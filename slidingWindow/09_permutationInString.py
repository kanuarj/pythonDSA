def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    s1Count, s2Count = [0]*26, [0]*26
    for i in range (len (s1)):
        s1Count[ord(s1[i]) - ord('a')] += 1
        s2Count[ord(s2[i]) - ord('a')] += 1

    matches = 0
    for i in range (26):
        matches += (1 if s1Count[i] == s2Count[i] else 0)

    first = 0
    for second in range (len (s1), len (s2)):
        if matches == 26:
            return True

        index = ord (s2[second]) - ord ('a')
        s2Count[index] += 1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] + 1 == s2Count[index]:
            matches -= 1

        index = ord (s2[first]) - ord ('a')
        s2Count[index] -= 1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] - 1 == s2Count[index]:
            matches -= 1

        first += 1
    return matches == 26

if __name__ == '__main__':
    s1 = 'ab'
    s2 = 'eidbaooo'
    print (checkInclusion (s1, s2))
