class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        dic = {}
        
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
                
        for key,value in dic.items():
            
            if value is not 1:
                return True
            
        return False
        