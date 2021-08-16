class Solution:
    
    def backspace(self, arg):
        result = []
        
        for val in arg:
            if val != '#':
                result.append(val)
            elif result:
                result.pop()
        
        return "".join(result)
            
        
    def backspaceCompare(self, s: str, t: str) -> bool:
        
                
        return self.backspace(s) == self.backspace(t)
        