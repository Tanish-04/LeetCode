class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:


        n = 0
        m = n + 1

        while n < len(arr):

            while m < len(arr):
                if (arr[n] == arr[m] * 2) or (arr[n] * 2 == arr[m]):
                    return True
                else:
                    m += 1

            n += 1
            m = n + 1

        return False
