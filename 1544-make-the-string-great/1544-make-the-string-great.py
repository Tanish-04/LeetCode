class Solution:
    def makeGood(self, s: str) -> str:
        
        # Approach Using Extra Space
        # Time Complexity O(n)
        # Space Complexity O(n)
        stack = []
        
        for i in s:
            if len(stack) == 0:
                stack.append(i)
            elif stack[-1] == i.swapcase():
                stack.pop()
            else:
                stack.append(i)
        
        return "".join(stack)
    