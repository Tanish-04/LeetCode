class MinStack:

    # Time Complexity O(1)
    # Space Complexity O(n)
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A = []
        self.Min = []
        

    def push(self, val: int) -> None:
        self.A.append(val)
        if not self.Min:
            self.Min.append(val)    
        else:
            x = self.Min.pop()
            self.Min.append(x)
            if val <= x:
                self.Min.append(val)
            else:
                self.Min.append(x)
        
    def pop(self) -> None:
        self.A.pop()
        self.Min.pop()

    def top(self) -> int:
        return self.A[-1]

    def getMin(self) -> int:
        x = self.Min.pop()
        self.Min.append(x)
        return x

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()