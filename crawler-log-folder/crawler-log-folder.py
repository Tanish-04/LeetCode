class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        result = []
        
        for i in logs:
            
            if i == '../' and len(result) != 0:
                result.pop()
            elif i == '../':
                pass
            elif i == './':
                pass
            else:
                result.append(i)
                
        return len(result)