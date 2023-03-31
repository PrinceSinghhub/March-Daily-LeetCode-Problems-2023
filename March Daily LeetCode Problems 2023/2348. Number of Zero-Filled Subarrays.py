class Solution:
    def zeroFilledSubarray(self, nums):

        cur = 0
        res = 0
        for num in nums:
            if num == 0:
                cur += 1
            else:
                res += cur + cur * (cur - 1) // 2
                cur = 0
        res += cur + cur * (cur - 1) // 2
        return res