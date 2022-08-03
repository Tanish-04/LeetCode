class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
         
        # Breaking the question into steps:
        # Assign count of every element into new Array starting value in new array from index 1
        # Find out count 2 and 0 for missing and duplicate value
        
            
            
        # Find repeated and missing one
        repeated = 0
        missing = 0
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
            