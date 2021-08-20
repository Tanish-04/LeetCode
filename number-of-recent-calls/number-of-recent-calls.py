class RecentCounter:

    def __init__(self):
        self.stack = []
        

    def ping(self, t: int) -> int:
        
        self.stack.append(t)
        start_range = t-3000
        while(self.stack[0] < start_range):
            self.stack.pop(0)

        return len(self.stack)
        


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)