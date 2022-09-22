class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        
        stack = []
        answer = []
        
        def helper(openP, closeP):
            
            if openP == closeP == n:
                answer.append("".join(stack))
                return
            
            if openP < n:
                stack.append("(")
                helper(openP+1,closeP)
                stack.pop()
            
            if openP > closeP:
                stack.append(")")
                helper(openP, closeP+1)
                stack.pop()
                
        
        helper(0,0)
        return answer