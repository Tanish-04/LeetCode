class Solution:
    def isValid(self, s: str) -> bool:
        
        # Time Complexity: O(n)
        # Space Complexity:O(n)
        
        stack = []
        
        for i in s:
            
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            
            # This elif will run when string s starting with closing ')]}'
            # so in that case valid parentheses condition will always be false
            
            elif len(stack) == 0: 
                return False
            # If forward parenthesis exist pop that element or return False
            
            elif i == ')' and stack.pop() != '(':
                return False
            
            elif i == ']' and stack.pop() != '[':
                return False
            
            elif i == '}' and stack.pop() != '{':
                return False
                
        if len(stack) == 0:
            return True
        
        return False
        