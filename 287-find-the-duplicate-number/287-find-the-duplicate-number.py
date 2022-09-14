class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        d = dict()
        
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
                
        for key,value in d.items():
            if d[key] >= 2:
                return key