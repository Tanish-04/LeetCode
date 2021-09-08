class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        
        # 23,11,9,16,3,18,3,9,5
        
        i = 1
        output = keysPressed[0]
        index = 0
        maxi = releaseTimes[0]
        while i < len(releaseTimes):
            if releaseTimes[i] - releaseTimes[i-1] > maxi:
                output = keysPressed[i]
                maxi = releaseTimes[i] - releaseTimes[i-1]
                index = i
            elif releaseTimes[i] - releaseTimes[i-1] == maxi:
                if ord(keysPressed[index]) < ord(keysPressed[i]):
                    output = keysPressed[i]
                    
            i += 1
                
        return output
        