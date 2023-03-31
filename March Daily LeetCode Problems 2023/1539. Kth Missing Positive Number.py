class Solution:
    def findKthPositive(self, arr,k):
        cout = 1
        ans = 1

        if k == 1:
            while True:
                if ans in arr:
                    ans += 1
                elif ans not in arr:
                    return ans
        while True:
            if cout == k:
                return ans
            elif ans in arr:
                ans += 1
            elif ans not in arr:
                ans += 1
                cout += 1
        return ans

arr = [1,2]
k = 1

ans = Solution()
print(ans.findKthPositive(arr,k))
