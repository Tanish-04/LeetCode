class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        # Time Complexity O(n)
        # Space Complexity O(n)
        
        '''
        Start from left of the string because left most integer are the highest so left(highest) --> right(lowest)
        so if we found that left is greater than its adjacent right then we pop that left value so that we can
        find our smallest digit from num
        '''
    
        stack = []
        
        for current in num:
            while k > 0 and len(stack) > 0 and current < stack[-1]:
                k -= 1
                stack.pop()
            stack.append(current)
        
        
        if k > 0:
            stack = stack[:-k]
            
            
        return "".join(stack).lstrip("0") or "0"
            
            
        