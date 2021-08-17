class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        N = len(digits)-1
        for i in range(N,-1,-1):
            digits[i] += 1
            if digits[i] > 9:
                digits[i] = 0
            else:
                return digits
             
            
        digits.insert(0,1)
        return digits
                