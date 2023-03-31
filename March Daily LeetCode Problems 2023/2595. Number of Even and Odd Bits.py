class Solution:
    def evenOddBit(self, n):

        ans = [0, 0]

        Bits = bin(n)[2::]

        print(Bits)
        rev = len(Bits)-1

        for i in range(len(Bits)):
            if int(Bits[i]) == 1 and rev % 2 == 0:
                ans[0] += 1

            elif int(Bits[i]) == 1 and rev % 2 != 0:
                ans[1] += 1

            rev-=1

        return ans

ans = Solution()
n = 17
print(ans.evenOddBit(n))