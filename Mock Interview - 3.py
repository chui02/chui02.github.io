from collections import deque
class Stacks:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, deque()
    def pop(self) -> int:
        return self.q1.popleft()
    
    def top(self) -> int:
        return self.q1[0]
    
    def empty(self) -> bool:
        return not self.q1
    
s = Stacks()    
s.push(1)
s.push(2)
print(s.top())
print(s.pop())
print(s.empty())