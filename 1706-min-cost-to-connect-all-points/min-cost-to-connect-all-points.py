class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, v):
        while v != self.par[v]:
            self.par[v] = self.par[self.par[v]]
            v = self.par[v]
        return v
    
    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)

        if p1 == p2:
            return False
        
        if p1 > p2:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                distance = abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1])
                heapq.heappush(edges, [distance, i, j])
        
        uf = UnionFind(len(points))
        mst_weight = 0
        
        while edges:
            distance, v1, v2 = heapq.heappop(edges)
            if uf.union(v1, v2):
                mst_weight += distance
        
        return mst_weight