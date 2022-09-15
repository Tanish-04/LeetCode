class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        size = len(height)
        
        left = 0
        right = size - 1
        
        maxHeight = size - 1
        area = 0
        
        for width in range(maxHeight,0,-1):
            
            if height[left] < height[right]:    
                area = max(area, width * height[left])
                left += 1
            
            else:
                area = max(area, width * height[right])
                right -= 1
                
        return area