class Solution:
    def makeGood(self, s: str) -> str:
        
        # Approach # 1 Using Extra Space
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
    
    
#         while i < len(s)-1:
#             if s[i] == s[i+1]:
#                 i += 1
#             elif s[i].lower() == s[i+1] or s[i].upper() == s[i+1]:
#                 s = s[:i] + s[i+2:]
#                 i = 0
#             else:
#                 i += 1
        
#         return s