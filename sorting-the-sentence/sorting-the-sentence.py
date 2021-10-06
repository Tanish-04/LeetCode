class Solution:
    def sortSentence(self, s: str) -> str:
        
        ArrayOfStrings = s.split()
        result = ArrayOfStrings.copy()
        
        for i in range(len(ArrayOfStrings)):
            idx = int((ArrayOfStrings[i][-1]))-1
            print(idx)
            result[idx] = ArrayOfStrings[i][:-1]
        
        return " ".join(result)
            
        
        
            
        