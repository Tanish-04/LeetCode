class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        
        # Time Complexity O(n)
        # Space Complexity O(n)
        ans, s = [0]*len(T), deque()
        for cur, cur_tmp in enumerate(T):
            while s and cur_tmp > T[s[-1]]:
                ans[s[-1]] = cur - s[-1]
                s.pop()
            s.append(cur)
        return ans





