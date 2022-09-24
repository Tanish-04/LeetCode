class Solution:
    def climbStairs(self, n: int) -> int:
        
        #Recursion
        # Time Limit Exceed error, use iterative method instead
#         if n < 2:
#             return 1
        
#         return self.climbStairs(n-1) + self.climbStairs(n-2)
        
        
        # Iterative Approach
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
    
    
    
        