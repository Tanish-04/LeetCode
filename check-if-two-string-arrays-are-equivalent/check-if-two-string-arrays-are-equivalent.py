class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        string = ""
        for i in word1:
            string += i
        
        string2 = ""
        for i in word2:
            string2 += i
            
        if string == string2:
            return True
        
        return False
        