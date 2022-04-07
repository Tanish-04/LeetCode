class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        addSet = set()
        l = 0
        result = 0
        
        for i in range(len(s)):
            while s[i] in addSet:
                addSet.remove(s[l])
                l += 1
            addSet.add(s[i])
            result = max(result,i-l+1)
            
        return result
    
    