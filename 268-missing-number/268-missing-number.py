class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        
        # Using XOR Logic
        
        missingNumber = len(nums)
        
        for i in range(len(nums)):
            
            missingNumber ^= i
            missingNumber ^= nums[i]
            
        return missingNumber
    
        
    
    
            
        
        