class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
         
        # Find repeated and missing one
        repeated = -1
        missing = 1
        # Declaring new array
        newArray = [0] * (len(nums) + 1)
        
        # Assigning count of numbers into new array
        for i in range(len(nums)):
            newArray[nums[i]] += 1
            
        # [0,1,2,0,1]
        
        for i in range(1,len(newArray)):
            if newArray[i] == 0:
                missing = i
            elif newArray[i] == 2:
                duplicate = i
        
        return duplicate,missing
            
        
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
#         result = []  
        
#         for i in range(len(nums)):
#             temp = abs(nums[i])-1
            
#             if nums[temp] < 0:
#                 result.append(temp+1)
#                 continue
#             nums[temp] = abs(nums[temp]) * -1
        
#         for i in range(len(nums)):
#             if nums[i] > 0 :
#                 result.append(i+1)
                
#         return result
            