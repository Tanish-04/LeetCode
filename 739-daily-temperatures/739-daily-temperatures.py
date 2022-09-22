class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        
        # Time Complexity O(n)
        # Space Complexity O(n)
        
        ans, stack = [0]*len(T), deque()
        
        for index, temp in enumerate(T):
            while stack and temp > T[stack[-1]]:
                ans[stack[-1]] = index - stack[-1]
                stack.pop()
            stack.append(index)
        return ans





