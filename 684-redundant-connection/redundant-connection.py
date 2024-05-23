class Union:
    def __init__(self, n):
        self.parent = {}
        self.power = {}

        for i in range(1, n + 1):
            self.parent[i] = i
            self.power[i] = 0
    
    def find(self, n):
        curr = self.parent[n]
        while curr != self.parent[curr]:
            self.parent[curr] = self.parent[self.parent[curr]]
            curr = self.parent[curr]
        return curr
    
    def connect(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return False

        if self.power[px] > self.power[py]:
            self.parent[py] = px
        elif self.power[py] > self.power[px]:
            self.parent[px] = py
        else:
            self.parent[py] = px
            self.power[px] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        union = Union(len(edges))
        for x, y in edges:
            if not union.connect(x, y):
                return [x, y]