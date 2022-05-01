class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        # Time Complexity O(n)
        # Space Complexity O(n)
        
        dic = {}
        
        for i in range(len(nums)):
            if nums[i] in dic and (abs(dic[nums[i]] - i) <= k):
                return True
            else:
                dic[nums[i]] = i
        
        return False
        