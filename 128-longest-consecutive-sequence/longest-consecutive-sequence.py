class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}
        for i in range(n):
            self.par[i] = i
            self.rank[i] = 1
    
    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        
        return p
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return 
        
        if self.rank[px] > self.rank[py]:
            self.par[py] = px
            self.rank[px] += self.rank[py]
        else:
            self.par[px] = py
            self.rank[py] += self.rank[px]

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        union = UnionFind(len(nums))
        numbers = {}
        for i, num in enumerate(nums):
            numbers[num] = i

        for i, num in enumerate(nums):
            if num + 1 in numbers:
                union.union(i, numbers[num + 1])
            elif num - 1 in numbers:
                union.union(i, numbers[num - 1])
        
        mergedNums = defaultdict(list)
        for num, i in numbers.items():
            leader = union.find(i)
            mergedNums[leader].append(num)
            
        maxLength = 0
        for merge in mergedNums.values():
            maxLength = max(maxLength, len(merge))
        
        return maxLength