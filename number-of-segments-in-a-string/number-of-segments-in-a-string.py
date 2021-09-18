class Solution:
    def countSegments(self, s: str) -> int:
        
        count = 0
        for i in s.split(" "):
            if i != "":
                count+=1
        return count


