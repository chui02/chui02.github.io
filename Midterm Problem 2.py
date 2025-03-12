def longPalString(s: str) -> str:
    n = len(s)
    if n == 0: #If empty
        return ""
    table = [[False] * n for _ in range(n)]
    indx = 0       #Index of longest palindrome
    maxLength = 1   #Max length of palindrome

    for i in range(n):  #Palindromes are subtrings of 1 length
        table[i][i] = True

    # Check for substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            table[i][i + 1] = True
            indx = i
            maxLength = 2

    for length in range(3, n + 1):  # Length from 3 to n
        for i in range(n - length + 1):
            #End of index
            j = i + length - 1
            if s[i] == s[j] and table[i + 1][j - 1]:
                table[i][j] = True
                indx = i
                maxLength = length
    return s[indx: indx + maxLength]

example1 = ["babad"]
for test in example1:
    print(f"Input string: {test}\nOutput: {longPalString(test)}")
