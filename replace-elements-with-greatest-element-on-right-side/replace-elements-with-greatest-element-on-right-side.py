class Solution:
    
    # User defined function created to select the maximum element from array
    
    def greaterElement(self,arg):
        result = 0
        
        for i in arg:
            if result < i:
                result = i
        
        return result
        
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        # Iterate over the array and select max element
        # from the right side and replace our element with that max value
        
        for i in range(len(arr)):
            arr[i] = self.greaterElement(arr[i+1:])
        
        arr[-1] = -1    
        
        return arr
        