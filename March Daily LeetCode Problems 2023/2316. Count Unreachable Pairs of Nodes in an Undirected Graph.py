class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        adjacency = defaultdict(list)
        neighours = defaultdict(list)
        for u, v in edges:
            adjacency[u].append(v)
            adjacency[v].append(u)
        pairs, component, rem = 0, 0, n
        visited = [False] * n
        for i in range(0, n):
            if not visited[i]:
                component = self.dfs(adjacency, visited, i)
                pairs += component * (rem - component)
                rem -= component
        return pairs

    def dfs(self, graph, visited, src):
        count = 1
        visited[src] = True

        if src not in graph:
            return count
        for neighour in graph[src]:
            if not visited[neighour]:
                count += self.dfs(graph, visited, neighour)

        return count