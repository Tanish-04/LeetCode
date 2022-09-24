class Solution:
    
    def fib(self, n: int) -> int:
        
        # Recursion
        
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        return self.fib(n-1) + self.fib(n-2)
        
        
        # Iterative 
#         firstNumber = 0
#         secondNumber = 1
        
#         if n == 1:
#             return secondNumber
#         if n == 0:
#             return firstNumber
        
#         result = 0
        
#         for i in range(2,n+1):
#             result = firstNumber + secondNumber
#             firstNumber = secondNumber
#             secondNumber = result
            
#         return result