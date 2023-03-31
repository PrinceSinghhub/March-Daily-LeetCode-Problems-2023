class Solution:
    def minEatingSpeed(self, piles,h):

        First = 1
        end = max(piles)

        while First < end:
            mid = int(First+(end-First) // 2)
            hourse =[(i + mid - 1) // mid for i in piles]
            if sum(hourse) > h:
                First = mid+1
            else:
                end = mid
        return First