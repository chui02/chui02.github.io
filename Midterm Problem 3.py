def anagram(s: str, t: str) -> bool:
    charLimit = [0] * 26 #Limit of alphabet
    for i in range(len(s)): #Counts the char occurrences in s and t
        charLimit[ord(s[i]) - ord('a')] += 1
        charLimit[ord(t[i]) - ord('a')] -= 1
    return all(count == 0 for count in charLimit) #If all counts are zero, the strings are anagrams

print(anagram("anagram", "nagaram"))
print(anagram("rat", "car"))