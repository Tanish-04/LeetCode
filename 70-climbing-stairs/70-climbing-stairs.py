class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        firstNumber = 1
        secondNumber = 1
        if n == 1:
            return firstNumber
        
        result = firstNumber + secondNumber
        for i in range(2,n+1):
            result = firstNumber + secondNumber
            firstNumber = secondNumber
            secondNumber = result
            
        return result
    
    
    
        