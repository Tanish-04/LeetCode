class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        low, medium, high = 0,0,len(nums)-1
        
        while medium <= high:
            if nums[medium] == 0:
                nums[low],nums[medium] = nums[medium],nums[low]
                low += 1
                medium += 1
            elif nums[medium] == 2:
                nums[medium],nums[high] = nums[high],nums[medium]
                high -= 1
            else:
                medium += 1
                
        return nums
                