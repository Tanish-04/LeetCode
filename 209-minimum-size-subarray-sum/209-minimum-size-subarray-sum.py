class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        # Optimized Approach
        # Sliding window
        
        # Time Complexity: O(n+m)
        # Space Complexity: O(1)    
        
        wind_start = wind_end = Sum = 0
        minimal_len = sys.maxsize
        while(wind_end < len(nums)):
            Sum += nums[wind_end]
            
            while(Sum >= target):
                minimal_len = min(minimal_len,wind_end-wind_start+1)
                Sum -= nums[wind_start]
                wind_start += 1
                
            wind_end += 1
            
        return minimal_len if minimal_len != sys.maxsize else 0
                
        
        
        
#         Burte force approach
        
#         Time Complexity : O(n)
#         Space Complexity : O(1)
#         minimal_len = sys.maxsize
        
#         for i in range(len(nums)):
#             Sum = 0
#             for j in range(i,len(nums)):
#                 Sum += nums[j]
                
#                 if Sum >= target:
#                     minimal_len = min(minimal_len,j-i+1)
#                     break
                    
        
#         return minimal_len if minimal_len != sys.maxsize else 0
        
        