class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {}
        for i in range(len(nums)):
            otherPair = target - nums[i]
            if (otherPair in dic):
                return [dic[otherPair], i]
            dic[nums[i]] = i