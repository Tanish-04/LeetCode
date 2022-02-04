class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        #  0 1 2 3  4 5 6 7 8
        # [9,4,2,10,7,8,8,1,9]
        maximum = 1
        start = 0
        end = 0
        length = len(arr)
        
        while start < length-1:
            if arr[start] == arr[start+1]:
                start += 1
                continue
            end = start + 1
            while(end < (length-1) and ( (arr[end] > arr[end-1] and arr[end] > arr[end+1]) or (arr[end] < arr[end-1]) and (arr[end] < arr[end+1]) ) ):
                end += 1
                
            maximum = max(maximum, end-start+1)
            start = end
            
        return maximum
        
    

                
                

        