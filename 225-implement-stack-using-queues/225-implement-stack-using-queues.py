class MyStack:

    def __init__(self):
        
        self.queue1 = []
        self.queue2 = []
        self.topval = 0
        

    def push(self, x: int) -> None:
        self.queue1.append(x)
        self.topval = x

    def pop(self) -> int:
        
        
        
        while len(self.queue1) > 1:
            self.topval = self.queue1.pop(0)
            self.queue2.append(self.topval)
            
        temp = self.queue1.pop(0)
        self.queue1 = self.queue2
        self.queue2 = []
        return temp    

    def top(self) -> int:
        return self.topval

    def empty(self) -> bool:
        return len(self.queue1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()