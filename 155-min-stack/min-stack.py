class MinStack:

    def __init__(self):
        self.stack = []
        self.min_ele = float('inf')
        

    def push(self, value: int) -> None:
        if not self.stack:
            self.min_ele = value
            self.stack.append(value)
        else:
            if value >= self.min_ele:
                self.stack.append(value)
            elif(value < self.min_ele):
                element = 2 * value - self.min_ele
                self.stack.append(element)
                self.min_ele = value
        

        

    def pop(self) -> None:
        if self.stack[-1] >= self.min_ele :
            self.stack.pop()
        elif self.stack[-1] < self.min_ele:
            self.min_ele = 2*self.min_ele - self.stack[-1]
            self.stack.pop()
        

    def top(self) -> int:
        if self.stack[-1] >= self.min_ele :
            return self.stack[-1]
        elif self.stack[-1] < self.min_ele:
            return self.min_ele
        
        

    def getMin(self) -> int:
        return self.min_ele


        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()