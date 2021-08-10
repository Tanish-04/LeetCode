class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        j = 1
        
        nums.sort()
        
        for i in nums:
            if j == i:
                j += 1
                
        return j
            
        