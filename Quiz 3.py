def prefixString(strs):
    #For empty cases
    if not strs:
        return ""
    strs.sort()
    first, last = strs[0], strs[-1]
    i = 0
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1
    return first[:i]

#Example test cases
inputsTests = [
    (["flower", "flow", "flight"], "fl"),   #Expected output in second brackets
    (["dog", "racecar", "car"], ""),
    (["banana"], "banana"),   #One string test
    (["", "egg"], ""),          #Empty string test
]

for i, (inp, expected) in enumerate(inputsTests, 1):
    result = prefixString(inp)
    print(f"Test #{i} {inp} output: {result}")