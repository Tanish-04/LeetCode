class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        num = 0
        for i in range(len(nums)):
            num += nums[i]
            nums[i] = num
            
        return nums