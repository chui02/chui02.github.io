def lexNumber(n):
    result = []
    
    def dfs(curr):
        if curr > n:
            return
        result.append(curr)
        for i in range(10):
            nextNumber = curr * 10 + i
            if nextNumber > n:
                return
            dfs(nextNumber)

    for i in range(1, 10):
        if i > n:
            break
        dfs(i)
    return result

inputs = [13, 2]
for n in inputs:
    print(f"Input: n = {n}")
    print(f"Output: {lexNumber(n)}\n")
