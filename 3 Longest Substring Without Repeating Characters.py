def lengthOfLongestSubstring(s):
    charsInSub = set()
    l = 0
    maxLength = 0
    currentLength = 0
    for r in range (len(s)):
        while s[r] in charsInSub:
            charsInSub.remove(s[l])
            l += 1
        charsInSub.add(s[r])
        currentLength = r - l + 1
        maxLength = max(maxLength, currentLength)
    return maxLength


s = "abcaabb"
print(lengthOfLongestSubstring(s))

