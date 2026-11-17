class MinStack:

    def __init__(self):
        self.stack = []
        self.ss = [] # supporting stack
        

    def push(self, value: int) -> None:
        self.stack.append(value)

        if (len(self.ss) == 0 or self.ss[-1] >= value):
            self.ss.append(value)
        

    def pop(self) -> None:      
        ans = self.stack[-1]
        self.stack.pop()

        if (self.ss[-1] == ans):
            self.ss.pop()
        return ans
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.ss[-1]
       


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()