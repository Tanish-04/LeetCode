
        
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
    
        
        # Using Hashmap
        cumsum = collections.Counter({0:1})
        Sum = 0
        count = 0
        for i in range(len(nums)):
            Sum += nums[i]
            count += cumsum[Sum-k]
            cumsum[Sum] += 1
            
        return count
            
        
        
        
        
        # Brute Force apporach
        # Time Complexity: O(n2)
        # Space Complexity: O(1)
#         length = 0
#         for i in range(len(nums)):
#             Sum = 0
#             for j in range(i,len(nums)):
#                 Sum += nums[j]
                
#                 if Sum == k:
#                     length += 1
                    
#         return length
                    
                    
                    