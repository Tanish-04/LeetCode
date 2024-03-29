class Solution:
    def mySqrt(self, x: int) -> int:
        
        
        left = 0
        right = x
        
        if x <= 1:
            return x
        
        
        while left < right:
            
            mid = left + (right - left) // 2
            if mid * mid == x:
                return mid
            if mid * mid < x:
                left = mid + 1
            else:
                right = mid
        
        
        return left-1
            
        
        