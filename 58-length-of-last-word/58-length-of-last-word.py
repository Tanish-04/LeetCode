class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        
        # Time Complexity O(n)
        # Space Complexity O(1)
        '''
        Iterate on array from the right and if space exist before any word
        appear then decrement i and if any character occurs start counting
        until it doesn't find space when iterating towards the left when
        space found then return that wordlength
        '''
        wordLength = 0
        
        for i in range(len(s)-1,-1,-1):
            if s[i] != ' ':
                wordLength += 1
            
            elif wordLength > 0:
                return wordLength
            
        return wordLength
        
        