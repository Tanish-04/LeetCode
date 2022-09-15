class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        pivotIndex = 0
        Sum = 0
        i = 0
        n = len(nums)
        
        while i < n:
            if sum(nums[0:i]) == sum(nums[i+1:n]):
                return i
            i += 1
        
        return -1
        
        
        