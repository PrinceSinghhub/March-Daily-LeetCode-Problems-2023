class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        uf = UnionFind(list(range(n)))
        redundant, wires = 0, n - 1

        for start, end in connections:
            if uf.union(start, end):
                wires -= 1
            else:
                redundant += 1

        return wires if wires <= redundant else -1


class UnionFind:
    def __init__(self, parent):
        self.parent = parent

    def find(self, node):
        while self.parent[node] != node:
            node = self.parent[node]
        return node

    def union(self, x, y):
        parent_x, parent_y = self.find(x), self.find(y)

        if parent_x == parent_y:
            return False
        if parent_x < parent_y:
            self.parent[parent_y] = parent_x
        else:
            self.parent[parent_x] = parent_y
        return True