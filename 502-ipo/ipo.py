class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfit = []
        minCapital = [(c, p) for p, c in zip(profits, capital)]
        heapq.heapify(minCapital)

        for i in range(k):
            while len(minCapital) and minCapital[0][0] <= w:
                (c, p) = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -1 * p)
            if not len(maxProfit):
                break
            w += -1 * heapq.heappop(maxProfit)
        
        return w