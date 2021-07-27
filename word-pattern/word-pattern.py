class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        listOfString = s.split(' ')
        
        dic = {}
        
        if len(listOfString) != len(pattern):
            return False
        
        keys = dic.keys()
        values = dic.values()
        
        for i in range(len(pattern)):
            if pattern[i] not in keys:
                if listOfString[i] in values:
                    return False
                else:
                    dic[pattern[i]] = listOfString[i]
                    
            else:
                if dic[pattern[i]] != listOfString[i]:
                    return False
                
        return True
                