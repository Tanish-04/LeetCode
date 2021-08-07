class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        
        result = 0
        remainder = 0
        original = x
        
        while x:
            remainder = x % 10
            result = result * 10 + remainder
            x = x // 10
            
        return result == original
            
        
        
        
        
        
        
        
        