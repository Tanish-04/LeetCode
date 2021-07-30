class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        dic = {}
        
        for i in range(len(order)):
            dic[order[i]] = i
        
        for i in range(len(words)-1):
            min_length = min(len(words[i]),len(words[i+1]))
            
            boolean = False
            for j in range(min_length):
                
                if dic[words[i][j]] > dic[words[i+1][j]]:
                    return False
                elif dic[words[i][j]] < dic[words[i+1][j]]:
                    boolean = True
                    break
            
            if not boolean and len(words[i]) > len(words[i+1]):
                return False
        return True
        