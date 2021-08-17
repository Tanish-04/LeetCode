class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        maximum = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maximum:
                result.append(True)
            else:
                result.append(False)
                
        return result
        