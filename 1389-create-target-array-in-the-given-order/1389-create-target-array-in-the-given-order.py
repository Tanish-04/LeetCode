class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
        targetArray = []
        n = len(nums)
        i = 0
        
        while i < n:
            targetArray.insert(index[i], nums[i])
            i += 1
            
        return targetArray