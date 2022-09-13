class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        
        for Width in range( int(sqrt(area)), 0, -1):
            if( area % Width == 0):
                return ((area // Width), Width)
            
        