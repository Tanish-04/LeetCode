class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        # Time Complexity O(n)
        # Space Complexity O(1)
        time = 0
        least = tickets[k]
        
        for i,value in enumerate(tickets):
            if i > k and value >=least:
                time += least-1
                
            elif value > least:
                time += least
            else:
                time += value
                
        return time
    
        
        
        