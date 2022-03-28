class Solution:
    def maxDepth(self, s: str) -> int:
        
        # Time Complexity O(n)
        # Space Complexity O(1)
#         maxDepth = depth = 0
        
#         for i in s:
#             if i == '(':
#                 depth += 1
#                 maxDepth = max(maxDepth,depth)
#             elif i == ')':
#                 depth -= 1
        
#         return maxDepth

        # Using Stack
        # Time Complexity O(n)
        # Space Complexity O(n)
    
        stack = []
        depth = 0
        
        for i in s:
            if i == '(':
                stack.append(i)
                depth = max(depth,len(stack))
            elif i == ')':
                stack.pop()
                
        return depth