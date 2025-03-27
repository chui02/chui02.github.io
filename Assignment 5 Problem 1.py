from collections import deque
class Solution:
    def removal(self, s: str):
        def check(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0
        queue = deque([s]) #BFS starts here
        tracked = set([s])
        found = False
        result = []
        while queue:
            size = len(queue)
            tracker = set()
            for _ in range(size):
                curr = queue.popleft()
                if check(curr):
                    result.append(curr)
                    found = True
                if found:
                    continue
                for i in range(len(curr)):
                    if curr[i] not in "()":
                        #Skips letters
                        continue  
                    charRemove = curr[:i] + curr[i + 1:]  #Removes  i-th character
                    if charRemove not in tracked:
                        queue.append(charRemove)
                        tracked.add(charRemove)
            if found:  #Stops at valid results
                break
        return result

sol = Solution()
print(sol.removal("()())()"))  #["(())()", "()()()"]
print(sol.removal("(a)())()")) #["(a())()", "(a)()()"]
print(sol.removal(")("))       #[""]
