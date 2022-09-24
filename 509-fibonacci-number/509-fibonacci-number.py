class Solution:
    
    def fib(self, n: int) -> int:
        
        firstNumber = 0
        secondNumber = 1
        
        if n == 1:
            return secondNumber
        if n == 0:
            return firstNumber
        
        result = 0
        
        for i in range(2,n+1):
            result = firstNumber + secondNumber
            firstNumber = secondNumber
            secondNumber = result
            
        return result