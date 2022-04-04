class Solution:
    def checkValidString(self, s: str) -> bool:
        
        open_parenthesis = []
        star = []
        
        for i in range(len(s)):
            if s[i] == '(':
                open_parenthesis.append(i)
            elif s[i] == '*':
                star.append(i)
            else:
                if len(open_parenthesis) != 0:
                    open_parenthesis.pop()
                elif len(star) != 0:
                    star.pop()
                else:
                    return False       
        
        while(len(open_parenthesis) != 0):
            if len(star) == 0:
                return False
            elif open_parenthesis[-1] < star[-1]:
                open_parenthesis.pop()
                star.pop()
            else:
                return False
        return True
        
        
        