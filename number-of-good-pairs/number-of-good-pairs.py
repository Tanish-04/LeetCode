class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        hashmap = {}
        
        resultCounter = 0
        
        for i in nums:
            
            if i not in hashmap:
                hashmap[i] = 1
            else:
                resultCounter += hashmap[i]
                hashmap[i] += 1
        
        return resultCounter