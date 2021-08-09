class Solution:
    
    def mergeSort(self,nums1):
            
            if len(nums1) > 1:
            
                mid = len(nums1) // 2
                left = nums1[:mid]
                right = nums1[mid:]
            
                self.mergeSort(left)
                
                self.mergeSort(right)
            
                i = j = k = 0
            
                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        nums1[k] = left[i]
                        i += 1
                    else:
                        nums1[k] = right[j]
                        j += 1
                
                    k += 1
                
                while i < len(left):
                    nums1[k] = left[i]
                    i += 1
                    k += 1
                
                while j < len(right):
                    nums1[k] = right[j]
                    j += 1
                    k += 1
                    
            return nums1        
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums1 += nums2
        result = self.mergeSort(nums1)
        
        length = math.ceil(len(result) / 2)
            
        if len(result) % 2 != 0:
            return result[length-1]
        else:
            return (result[length-1] + result[length])/2
                