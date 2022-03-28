class Solution:
    def maxDepth(self, s: str) -> int:
        
        # Time Complexity O(n)
        # Space Complexity O(1)
        maxDepth = depth = 0
        
        for i in s:
            if i == '(':
                depth += 1
                maxDepth = max(maxDepth,depth)
            elif i == ')':
                depth -= 1
        
        return maxDepth