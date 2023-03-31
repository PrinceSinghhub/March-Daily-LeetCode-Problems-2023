class Solution:
    def minPathSum(self, grid):
        if not len(grid) or not len(grid[0]):
            return 0

        m, n, cache = len(grid) - 1, len(grid[0]) - 1, {}

        return self.findMinSum(grid, m, n, cache)

    def findMinSum(self, grid, m, n, cache):
        if (m, n) in cache:
            return cache[(m, n)]
        elif m < 0 or n < 0:
            return float('inf')
        elif m == 0 and n == 0:
            return grid[0][0]
        else:
            cache[(m, n)] = grid[m][n] + min(self.findMinSum(grid, m - 1, n, cache), self.findMinSum(grid, m, n - 1, cache))

            return cache[(m, n)]