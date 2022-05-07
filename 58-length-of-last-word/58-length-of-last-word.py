class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        wordLength = 0
        
        for i in range(len(s)-1,-1,-1):
            if s[i] != ' ':
                wordLength += 1
            
            elif wordLength > 0:
                return wordLength
            
        return wordLength
        
        