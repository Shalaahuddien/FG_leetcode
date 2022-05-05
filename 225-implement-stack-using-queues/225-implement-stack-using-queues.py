class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.t = None

    def push(self, x: int) -> None:
        self.q1.append(x)
        self.t = x

    def pop(self) -> int:
        for _ in range(len(self.q1) - 1):
            self.t = self.q1.popleft()
            self.q2.append(self.t)
        ret = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return ret

    def top(self) -> int:
        return self.t

    def empty(self) -> bool:
        return len(self.q1) == 0
    
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()