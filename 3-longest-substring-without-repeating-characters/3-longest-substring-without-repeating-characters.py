class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        addSet = set()
        l = 0
        result = 0
        
        for r in range(len(s)):
            while s[r] in addSet:
                addSet.remove(s[l])
                l += 1
            addSet.add(s[r])
            result = max(result,r-l+1)
            
        return result
    
    