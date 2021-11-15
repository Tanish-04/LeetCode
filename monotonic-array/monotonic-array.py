class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        decreasingSeries = all([nums[i-1] >= nums[i] for i in range(1,len(nums))])
        increasingSeries = all([nums[i-1] <= nums[i] for i in range(1,len(nums))])
        
        return decreasingSeries or increasingSeries