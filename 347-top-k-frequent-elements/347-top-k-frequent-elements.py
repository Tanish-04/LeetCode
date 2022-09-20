class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency = [[] for i in range(len(nums)+1)]
        valuesCount = {}
        res = []
        
        for i in nums:
            if i not in valuesCount:
                valuesCount[i] = 1
            else:
                valuesCount[i] += 1
        
        for key,value in valuesCount.items():
            frequency[value].append(key)
        
        for n in range(len(frequency)-1,0,-1):
            for ele in frequency[n]:
                res.append(ele)
                if len(res) == k:
                    return res