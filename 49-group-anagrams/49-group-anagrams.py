class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = []
        dic = dict()
        
        for i in strs:
            s = "".join(sorted(i))
            
            if s not in dic:
                dic[s] = [i]
            else:
                dic[s].append(i)
                
        for key,value in dic.items():
            result.append(value)
            
        return result
            
            
        