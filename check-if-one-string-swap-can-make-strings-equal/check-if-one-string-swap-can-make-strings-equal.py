class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        # if Both are equals
        if s1 == s2:
            return True
        # first check every element which exist in s1 if exist in s2 then move to the next step 
        # otherwise return False
        for i in s1:
            if i not in s2:
                return False
            
        # checking every element from s1 into s2 if it doesn't exist at the right position then
        # add that element into the result array and if its length is 2 then swapping can be 
        # performed so we return True otherwise it will return False
        result = []
        
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                result.append(s2[i])
                
        if len(result) == 2:
            return True
        else:
            False
        