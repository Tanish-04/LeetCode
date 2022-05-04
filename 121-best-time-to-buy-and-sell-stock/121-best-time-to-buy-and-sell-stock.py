class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # kaden's algorithm pending
        # Approach 1
        '''
        Time Complexity: O(n)
        Space Compexity: O(1)
        '''
        left = 0 
        right = 1
        maxProfit = 0
        
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit,profit)
            else:
                left = right
            right += 1
        return maxProfit
    
        
        
        
        
        
        
        
    

    
        
        