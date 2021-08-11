class Solution:
    def reverse(self, x: int) -> int:
        
        result = int(str(abs(x))[::-1])
        print(2**31)
        if result < 2 ** 31:
            if x >= 0:
                return result
            else:
                return -result
        else:
            return 0
        