def maxSubstring(k, string):
    currentLength = 0
    maxLength = 0
    l = 0
    characters = set()
    for r in range(len(string)):
        characters.add(string[r])
        while len(characters) > k:
            characters.remove(string[l])
            l += 1
        currentLength = r - l + 1
        maxLength = max(currentLength, maxLength)
    return maxLength


substringChars = set()
    maxLength = 0
    l = 0
    for r in range(len(s)):
        while s[r] in substringChars:
            substringChars.remove(s[l])
            print("removed", s[l])
            l += 1
        substringChars.add(s[r])
        maxLength = max(maxLength, len(substringChars))
    return maxLength

inputstring = "qrsvbspk"
outputstring = lengthOfLongestSubstring(inputstring)
print(outputstring)

