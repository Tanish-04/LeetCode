class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        complement = {}
        
        for i in range(len(nums)):
            temp = target - nums[i] 
            if temp in complement:
                return [complement[temp],i]
            complement[nums[i]] = i
            
        return False
        
        