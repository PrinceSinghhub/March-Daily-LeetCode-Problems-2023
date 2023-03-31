class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        N = len(edges)

        def dfs(node, step):
            if node in total:
                return total[node]
            if node in visited:
                return step - visited[node]
            else:
                visited[node] = step
                next_node = edges[node]
                if next_node == -1:
                    return -1
                return dfs(next_node, step + 1)

        total = defaultdict(int)
        for e in range(len(edges)):
            if e not in total:
                visited = defaultdict(int)
                res = dfs(e, 0)
                for v in visited:
                    total[v] = res

        ans = max(total.values())

        if ans == 0:
            return -1
        return ans