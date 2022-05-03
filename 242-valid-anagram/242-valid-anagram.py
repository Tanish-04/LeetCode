class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        storedAnagram = dict()
        
        for i in s:
            if i in storedAnagram:
                storedAnagram[i] += 1
            else:
                storedAnagram[i] = 1
        
        
        for i in t:
            if i not in storedAnagram:
                return False
            else:
                storedAnagram[i] -= 1
        
        
        for val in storedAnagram.values():
            if val != 0:
                return False
        
        return True
        