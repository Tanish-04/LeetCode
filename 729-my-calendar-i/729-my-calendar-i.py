class MyCalendar:
    
    def __init__(self):
        self.dic = dict()

        

    def book(self, s1: int, e1: int) -> bool:
        
        for s2,e2 in self.dic.items():
            if (s1>=s2 and s1<e2) or (s2>=s1 and s2<e1):
                return False
        
        self.dic[s1] = e1
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)