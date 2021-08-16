class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        
        isGreater = False
        isLesser = False
        
        for i in range(1,len(nums)):
            
            if nums[i-1] > nums[i]:
                isGreater = True
            
            if nums[i-1] < nums[i]:
                isLesser = True
                
            
            if isGreater and isLesser:
                return False
            
        return True
        