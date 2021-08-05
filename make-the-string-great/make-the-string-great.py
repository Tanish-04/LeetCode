class Solution:
    def makeGood(self, s: str) -> str:
        
        '''Time Complexity: O(n)
        Space Complexity: O(n)
        
        Build Stack compare last inserted element with element of s and convert its case
        to check good string
        
        '''
        stack = []
        
        for i in s:
            if len(stack) == 0:
                stack.append(i)
            elif stack[-1] == i.swapcase():
                stack.pop()
            else:
                stack.append(i)
                
        return "".join(stack)
        