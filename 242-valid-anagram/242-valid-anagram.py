class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        '''
        Time Complexity(n+n+n => 3n => n)
        Space Complexity(n)
        Approach:
        Store str s into dictionary, and then use that dictionary to check 
        t value if doesn't exist stop there if exist -1 it's value so that
        at the end we can check if all values of key are 0 then it's anagram
        otherwise it's not
        '''
        
        storedAnagram = dict()
        
        for i in s:
            if i in storedAnagram:
                storedAnagram[i] += 1
            else:
                storedAnagram[i] = 1
        
        
        for i in t:
            if i not in storedAnagram:
                return False
            else:
                storedAnagram[i] -= 1
        
        
        for val in storedAnagram.values():
            if val != 0:
                return False
        
        return True
        