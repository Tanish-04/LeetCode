class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        
        
        for i in ops:
            if i == "C":
                stack.pop()
            elif i == "D":
                stack.append(stack[-1]*2)
            elif i == "+":
                a = stack.pop()
                b = stack[-1]+a
                stack.append(a)
                stack.append(b)
            else:
                stack.append(int(i))
                
        return sum(stack)
        