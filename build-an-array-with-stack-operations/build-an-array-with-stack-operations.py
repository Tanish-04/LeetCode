class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        arr = []
        count = 1
        i = 0
        
        while i < len(target):
            if target[i] == count:
                arr.append('Push')
                i += 1
            else:
                arr.append('Push')
                arr.append('Pop')
            count += 1
            
        return arr
            