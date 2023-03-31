from collections import deque
class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        if n == 0 or not connections:
            return 0
        paths = [[i] for i in range(n)]
        print(paths)
        for i, j in connections:
            paths[i].append(j)
            paths[j].append(i)
        order = [0 for i in range(n)]
        que = deque()
        node = 0
        que.append(node)
        count = 0
        while que:
            node = que.popleft()
            for i in paths[node]:
                if order[i] == 0:
                    count += 1
                    order[i] = count
                    que.append(i)
        res = 0
        print(order)
        for i, j in connections:
            if order[i] < order[j]:
                res += 1
        return res