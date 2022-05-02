class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # Time Complexity O(n)
        # Space Complexity O(n)
        
        dic = {}
        
        for i in range(len(nums)):
            dic[nums[i]] = i
            
        for i in range(len(nums)+1):
            if i not in dic:
                return i
            
        