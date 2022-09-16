class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        
        dic_s_t = dict()
        dic_t_s = dict()
        
        for c1,c2 in zip(s,t):
            
            if (c1 not in dic_s_t) and (c2 not in dic_t_s):
                dic_s_t[c1] = c2
                dic_t_s[c2] = c1
                print(dic_s_t)
                print(dic_t_s)
            elif dic_s_t.get(c1) != c2 or dic_t_s.get(c2) != c1:
                return False
            
        return True
        