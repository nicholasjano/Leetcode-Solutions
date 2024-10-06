class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, x, y):
        p1, p2 = self.find(x), self.find(y)
        if (p1 == p2):
            return False
        if (self.rank[p1] > self.rank[p2]):
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        uf = UnionFind(n)

        for edge in edges:
            uf.union(edge[0], edge[1])
        
        if (uf.find(source) == uf.find(destination)):
            return True
        return False