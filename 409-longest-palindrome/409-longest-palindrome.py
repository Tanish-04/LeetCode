class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        d = collections.Counter(s)
        result = 0
        isOdd = False
        for v in d.values():
            if v % 2 == 0:
                result += v
            else:
                result += (v-1)
                isOdd = True
        
        if isOdd:
            result += 1
            
        return result
