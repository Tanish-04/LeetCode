class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        '''Understanding Approach
        L/R-> Product
        [1,1,2,6]
        R/R-> Product
        [24,12,4,1]
        Then multiply together
        '''
        n = len(nums)
        left = [0] * n 
        right = [0] * n
        answer = [0] * n
        
        left[0] = 1
        for i in range(1,len(nums)):
            left[i] = left[i-1] * nums[i-1]
        
        right[n-1] = 1
        
        
        for j in range(n-2,-1,-1):
            right[j] = right[j+1]* nums[j+1]
        
        for i in range(n):
            answer[i] = left[i] * right[i]
            
        return answer
        
        
        
        
        