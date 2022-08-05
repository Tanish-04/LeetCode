class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        # [1,2,3,3,5]
        
        duplicated = 0
        missing = 0
        
        # newArray = [0,1,1,2,0,1]
        newArray = [0] * (len(nums) + 1)
        
        for i in range(len(nums)):
            newArray[nums[i]] += 1
        
        for i in range(1,len(newArray)):
            if newArray[i] == 2:
                duplicated = i
            elif newArray[i] == 0:
                missing = i
        
            if duplicated != 0 and missing != 0:
                break
        
        
        return duplicated,missing