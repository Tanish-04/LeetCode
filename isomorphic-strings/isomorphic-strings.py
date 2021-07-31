class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        dic_1 = {}
        dic_2 = {}
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            value_of_s = s[i]
            value_of_t = t[i]
            
            if value_of_s not in dic_1:
                dic_1[value_of_s] = i
            
            if value_of_t not in dic_2:
                dic_2[value_of_t] = i
                
            if dic_1[value_of_s] != dic_2[value_of_t]:
                return False
        
        return True