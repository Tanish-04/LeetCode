class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
          
        duplicate = 0
        missing = 0
        
        for i in range(len(nums)):
            temp = abs(nums[i])-1
            
            if nums[temp] < 0:
                duplicate = temp+1
                continue
            nums[temp] = abs(nums[temp]) * -1
        
        for i in range(len(nums)):
            if nums[i] > 0 :
                missing = i+1
                
        return duplicate,missing
            