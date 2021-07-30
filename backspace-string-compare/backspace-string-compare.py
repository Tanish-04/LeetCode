class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        result = []
        result2 = []
        
        for val in s:
            if val != '#':
                result.append(val)
            elif result:
                result.pop()
        
        for val in t:
            if val != '#':
                result2.append(val)
            elif result2:
                result2.pop()
                
        return "".join(result) == "".join(result2)
        