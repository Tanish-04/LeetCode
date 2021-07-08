class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max1 = 0
        max2 = 0
        
        for i in range(len(nums)):
            if max1 < nums[i]:
                max1 = nums[i]
                
        nums.remove(max1)
        
        for j in range(len(nums)):
            if max2 < nums[j]:
                max2 = nums[j]
                
        return (max1-1)*(max2-1)
        