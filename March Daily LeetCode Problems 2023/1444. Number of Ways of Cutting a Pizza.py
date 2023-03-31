MOD = 1000000007


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:

        m, n = len(pizza), len(pizza[0])

        @lru_cache(None)
        def dfs(k, i=0, j=0, res=0):

            if not (0 <= i < m and 0 <= j < n): return 0

            for x, y in product(range(i, m), range(j, n)):
                if pizza[x][y] == "A":
                    if not k: return 1
                    res += sum(dfs(k - 1, X, j) for X in range(x + 1, m))
                    break

            for y, x in product(range(j, n), range(i, m)):
                if pizza[x][y] == "A":
                    if not k: return 1
                    res += sum(dfs(k - 1, i, Y) for Y in range(y + 1, n))
                    break

            return res % MOD

        return dfs(k - 1)