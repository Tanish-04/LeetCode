class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        sums = nums[0]
        maxsum = nums[0]
        
        for i in range(1,len(nums)):
            
            if sums + nums[i] < nums[i]:
                sums = nums[i]
            else:
                sums += nums[i]
                
            if maxsum < sums:
                maxsum = sums
                
        return maxsum
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                