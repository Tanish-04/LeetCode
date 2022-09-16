class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
       
        
        
        firstPointer = 0
        secondPointer = 0
        s_n = len(s)
        t_n = len(t)
        
        while firstPointer < s_n and secondPointer < t_n:
            if s[firstPointer] == t[secondPointer]:
                firstPointer += 1
                secondPointer += 1
            else:
                secondPointer += 1
            
        return firstPointer == s_n
        