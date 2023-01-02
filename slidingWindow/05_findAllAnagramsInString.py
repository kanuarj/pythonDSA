def findAnagrams (s : str, p : str) -> list ():
    if len (p) > len (s):
        return []

    pCounter, sCounter = {}, {}
    for i in range (len (p)):
        pCounter[p[i]] = 1 + pCounter.get (p[i], 0)
        sCounter[s[i]] = 1 + sCounter.get (s[i], 0)

    result = [0] if sCounter == pCounter else []
    first = 0
    for second in range (len (p), len (s)):
        sCounter[s[second]] = 1 + sCounter.get (s[second], 0)
        sCounter[s[first]] -= 1

        if sCounter[s[first]] == 0:
            sCounter.pop (s[first])
        
        first += 1
        if sCounter == pCounter:
            result.append (first)
        
    return result


if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    print (findAnagrams (s, p))