class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A = []
        

    def push(self, val: int) -> None:
        self.A.append(val)

    def pop(self) -> None:
        self.A.pop()

    def top(self) -> int:
        return self.A[-1]

    def getMin(self) -> int:
        return min(self.A)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()