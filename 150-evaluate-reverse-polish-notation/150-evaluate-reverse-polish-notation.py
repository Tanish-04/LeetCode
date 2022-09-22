class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        for c in range(len(tokens)):
            if tokens[c] == "+":
                stack.append(stack.pop() + stack.pop())
            elif tokens[c] == "*":
                stack.append(stack.pop() * stack.pop())
            elif tokens[c] == "-":
                a,b = stack.pop(),stack.pop()
                stack.append(b-a)
            elif tokens[c] == "/":
                a,b = stack.pop(),stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(tokens[c]))
        return stack[-1]
                