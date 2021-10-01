class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        # Time Complexity : O(NlogN)
        # Space Complexity : O(N)
        
        
        target = sorted(heights)
        count = 0
        
        for i,value in enumerate(heights):
            if value != target[i]:
                count += 1
                
        return count
        
        