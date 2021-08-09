class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        result = string.ascii_lowercase
        
        for i in result:
            if i not in sentence:
                return False
        
        return True